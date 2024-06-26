import yaml
import requests
from time_recognition import date_to_epoch_timestamp
import datetime
from models.scrobble import Scrobble

DOMAIN = 'ws.audioscrobbler.com'
API_KEY: str
USER: str
COUNTER = {str: str}


class LastFm:

    def __init__(self, assets_file_path: str):
        """Accepts `assets_file_path` as a path to `assets.yml` file with fields `api_key` and `user_id`"""
        self.api_key: str | None = None
        self.user_id: str | None = None
        self._recent_tracks: dict[dict] = {}
        self._read_assets(assets_file_path)

    @property
    def scrobbles(self) -> list[Scrobble]:
        scrobbles: list[Scrobble] = []
        for item in self._recent_tracks:
            scrobbles += [Scrobble(item)]
        return scrobbles

    def get_recent_tracks(self, date_from: str = None, date_to: str = None) -> list[Scrobble]:
        if date_from is not None:
            date_from = date_to_epoch_timestamp(date_from)
        if date_to is not None:
            date_to = date_to_epoch_timestamp(date_to)
        # zip up json as into a list of Scrobble
        result: list[Scrobble] = []
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            _recent_tracks = self._get_recent_tracks(date_from, date_to, current_page)
            total_pages = int(_recent_tracks['recenttracks']['@attr']['totalPages'])
            current_page += 1
            for item in _recent_tracks['recenttracks']['track']:
                result += [Scrobble(item)]
        return result

    def accumulate(self):
        # TODO: return counter
        albums: dict[str, dict[str, int]] = {}
        for scrobble in self._recent_tracks:
            if 'date' not in scrobble: continue
            album = scrobble['album']['#text']
            day_uts = datetime.datetime.utcfromtimestamp(int(scrobble['date']['uts']))
            day = day_uts.strftime('%Y-%m-%d')
            if album not in albums: albums[album] = {}
            if day not in albums[album]: albums[album][day] = 0
            print(album, day, '1')
            albums[album][day] += 1
        return albums

    def _read_assets(self, file_path: str) -> dict:
        """Retrieving API_KEY for last fm"""
        with open(file_path, 'r') as file:
            assets = yaml.safe_load(file)
            self.api_key = assets['api_key']
            self.user_id = assets['user']
        return assets

    def _get_recent_tracks(self, date_from: int = None, date_to: int = None, page: int = 1) -> dict[dict]:
        request = ('http://' + DOMAIN
                   + '/2.0/?method=user.getRecentTracks'
                   + f'&api_key={self.api_key}'
                   + f'&user={self.user_id}'
                   + f'&page={page}'
                   + f'&limit=200'
                   + f'&format=json')
        if date_from is not None:
            request += f'&from={date_from}'
        if date_to is not None:
            request += f'&to={date_to}'
        response = self._send_request(request)
        return response

    def _send_request(self, request: str):
        response = requests.get(request)
        if response.ok is False:
            raise Exception(f"Response has status code {response.status_code}. Reason: {response.reason}. Text: {response.text}")
        recent_tracks = response.json()
        return recent_tracks


if __name__ == '__main__':

    LastFm = LastFm('input/assets.yml')
    recent_tracks = LastFm.get_recent_tracks()

    i = 1
    for track in recent_tracks:
        artist = track.artist
        album = track.album
        song = track.title

        print(f"{i}. {artist} – {album} – {song}")
        if album not in COUNTER: COUNTER[album] = 0
        COUNTER[album] += 1
        i += 1

    print(COUNTER)
