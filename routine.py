import lastfm

LastFm = lastfm.LastFm('assets.yml')

COUNTER = {}

tracks = LastFm.get_recent_tracks('2024-04-24', '2024-04-25')

i = 1
for track in tracks:
    artist = track['artist']['#text']
    album = track['album']['#text']
    song = track['name']

    print(f"{i}. {artist} – {album} – {song}")
    if album not in COUNTER: COUNTER[album] = 0
    COUNTER[album] += 1
    i += 1

print(COUNTER)
