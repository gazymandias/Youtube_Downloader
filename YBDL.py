from pytube import YouTube, Playlist
v = YouTube('https://www.youtube.com/watch?v=Y157xQg4lUE')

# Playlists must be unlisted or public
pl = Playlist('https://www.youtube.com/watch?v=RyW6zBjSq38&list=PLd6pevQQF7fshODm52Z42DMqpGgVOG-Fp')

# for some reason this is needed to get the length to work
pl.populate_video_urls()
print(f'Videos in playlist: {len(pl.video_urls)}')

playlist_urls = pl.video_urls

for url in playlist_urls:
    v = YouTube(url)
    # print(v.title)
    # print(v.streams.all())
    v.streams.first().download()

    print(url)

