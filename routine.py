import lastfm

LastFm = lastfm.LastFm('input/assets.yml')

COUNTER = {}

scrobbles = LastFm.get_recent_tracks('2024-05-01', '2024-05-31')

for sc in scrobbles:
    if sc.album not in COUNTER:
        COUNTER[sc.album] = {}
    if sc.date not in COUNTER[sc.album]:
        COUNTER[sc.album][sc.date] = 0
    COUNTER[sc.album][sc.date] += 1

i = 1
for album, scrobs in COUNTER.items():
    print(f"{i}. {album} – {scrobs}")
    i += 1
