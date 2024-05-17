import datetime


class Scrobble:
    """Scrobble object for, you guessed it, a scrobble"""

    raw: dict = None

    def __init__(self, raw_json):
        self.raw = raw_json

    @property
    def artist(self) -> str:
        return self.raw['artist']['#text']

    @property
    def title(self) -> str:
        return self.raw['name']

    @property
    def album(self) -> str:
        return self.raw['album']['#text']

    @property
    def date(self) -> str or None:
        epoch = self.date_uts
        if epoch is None:
            return None
        date = datetime.datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d')
        return date

    @property
    def date_uts(self) -> int or None:
        try:
            uts = int(self.raw['date']['uts'])
            return uts
        except KeyError:
            return None

