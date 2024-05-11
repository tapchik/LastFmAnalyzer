class Scrobble:
    """Scrobble object for, you guessed it, a scrobble"""

    raw: dict = None

    def __init__(self, raw_json):
        self.raw = raw_json

    @property
    def artist(self):
        return self.raw['artist']['#text']

    @property
    def title(self):
        return self.raw['name']

    @property
    def album(self):
        return self.raw['album']['#text']

    @property
    def date(self):
        return self.raw['uts']
