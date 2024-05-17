import lastfm
#import draw_chart

LastFm = lastfm.LastFm('input/assets.yml')

tracks = LastFm.get_recent_tracks('2024-01-01', '2024-01-31')

for scrobble in tracks:
    print(scrobble.artist, scrobble.album, scrobble.title)
