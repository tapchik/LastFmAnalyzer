import lastfm

LastFm = lastfm.LastFm('input/assets.yml')

COUNTER = {}
albums = {}

scrobbles = LastFm.get_recent_tracks('2024-05-01', '2024-05-31')

total_sum = 0
for sc in scrobbles:
    if sc.album not in COUNTER:
        COUNTER[sc.album] = {}
    if sc.date not in COUNTER[sc.album]:
        COUNTER[sc.album][sc.date] = 0
    COUNTER[sc.album][sc.date] += 1
    if sc.album not in albums: albums[sc.album] = 0
    albums[sc.album] += 1
    total_sum += 1

i = 1
for album, scrobs in COUNTER.items():
    tt = albums[album]
    print(f"{i}. {album} - total: {tt} – {scrobs}")
    i += 1

print(total_sum)
