import lastfm
#import draw_chart

LastFm = lastfm.LastFm('assets.yml')

tracks = LastFm.get_recent_tracks('2024-01-01', '2024-01-31')

albums = LastFm.accumulate()
print(albums)
