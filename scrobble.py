class track:
    """Draft of the class track, might not be used"""

    json = None

    def __init__(self, raw_json):
        self.json = raw_json

    @property
    def title(self):
        return self.json['name']

    def artist(self):
        return self.json['artist']['#text']

    def album(self):
        return self.json['album']['#text']
