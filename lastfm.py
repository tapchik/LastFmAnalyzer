import yaml
import requests
from time_recognition import date_to_epoch_timestamp

DOMAIN = 'ws.audioscrobbler.com'
API_KEY: str
USER: str
COUNTER = {str: str}


def read_assets(file_path: str) -> dict:
    """Retrieving API_KEY for last fm"""
    with open(file_path, 'r') as file:
        assets = yaml.safe_load(file)
    return assets


assets = read_assets('assets.yml')
API_KEY = assets['api_key']
USER = assets['user']


def template_request_recent_tracks():
    return ('http://' + DOMAIN
            + '/2.0/?method=user.getRecentTracks'
            + f'&api_key={API_KEY}'
            + f'&user={USER}'
            + '&format=json')


def template_request_recent_tracks_period(date_from: int, date_to: int):
    """Dates accepted as epoch timestamps"""
    return ('http://' + DOMAIN
            + '/2.0/?method=user.getRecentTracks'
            + f'&api_key={API_KEY}'
            + f'&user={USER}'
            + '&format=json'
            + f'&from={date_from}'
            + f'&to={date_to}')


class LastFm:

    def get_recent_tracks(self, date_from: str, date_to: str):
        epoch_date_from = date_to_epoch_timestamp(date_from)
        epoch_date_to = date_to_epoch_timestamp(date_to)
        request = template_request_recent_tracks_period(epoch_date_from, epoch_date_to)
        recent_tracks = self._send_request(request)
        return recent_tracks['recenttracks']['track']


    def _send_request(self, request):
        response = requests.get(request)
        recent_tracks = response.json()
        return recent_tracks


if __name__ == '__main__':

    response = requests.get(template_request_recent_tracks())
    recent_tracks = response.json()

    i = 1
    for track in recent_tracks['recenttracks']['track']:
        artist = track['artist']['#text']
        album = track['album']['#text']
        song = track['name']

        print(f"{i}. {artist} – {album} – {song}")
        if album not in COUNTER: COUNTER[album] = 0
        COUNTER[album] += 1
        i += 1

    print(COUNTER)
