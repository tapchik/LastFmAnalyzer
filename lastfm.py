import yaml
import requests
from time_recognition import date_to_epoch_timestamp

DOMAIN = 'ws.audioscrobbler.com'
API_KEY: str
USER: str
COUNTER = {str: str}


class LastFm:

    def __init__(self, assets_file_path: str):
        """Accepts `assets_file_path` as a path to `assets.yml` file with fields `api_key` and `user_id`"""
        self.api_key: str
        self.user_id: str
        self.recent_tracks: dict = {}
        self._read_assets(assets_file_path)

    def get_recent_tracks(self, date_from: str = None, date_to: str = None) -> dict:
        if date_from is not None and date_to is not None:
            epoch_date_from = date_to_epoch_timestamp(date_from)
            epoch_date_to = date_to_epoch_timestamp(date_to)
            request = self.template_request_recent_tracks_period(epoch_date_from, epoch_date_to)
        else:
            request = self.template_request_recent_tracks()
        self.recent_tracks = self._send_request(request)
        return self.recent_tracks['recenttracks']['track']

    def accumulate(self):
        # TODO: return counter
        t = self.recent_tracks
        return "yes"

    def _read_assets(self, file_path: str) -> dict:
        """Retrieving API_KEY for last fm"""
        with open(file_path, 'r') as file:
            assets = yaml.safe_load(file)
            self.api_key = assets['api_key']
            self.user_id = assets['user']
        return assets

    def _send_request(self, request):
        response = requests.get(request)
        recent_tracks = response.json()
        return recent_tracks

    def template_request_recent_tracks(self):
        return ('http://' + DOMAIN
                + '/2.0/?method=user.getRecentTracks'
                + f'&api_key={self.api_key}'
                + f'&user={self.user_id}'
                + '&format=json')

    def template_request_recent_tracks_period(self, date_from: int, date_to: int):
        """Dates accepted as epoch timestamps"""
        return ('http://' + DOMAIN
                + '/2.0/?method=user.getRecentTracks'
                + f'&api_key={self.api_key}'
                + f'&user={self.user_id}'
                + '&format=json'
                + f'&from={date_from}'
                + f'&to={date_to}')


if __name__ == '__main__':

    LastFm = LastFm('assets.yml')
    recent_tracks = LastFm.get_recent_tracks()

    i = 1
    for track in recent_tracks:
        artist = track['artist']['#text']
        album = track['album']['#text']
        song = track['name']

        print(f"{i}. {artist} – {album} – {song}")
        if album not in COUNTER: COUNTER[album] = 0
        COUNTER[album] += 1
        i += 1

    print(COUNTER)
