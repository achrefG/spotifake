from tinytag import TinyTag
def metadata(filepath):
    tag = TinyTag.get(filepath)
    print()
    print("artist", (tag.artist))
    print("album:", tag.album)
    print("title:", tag.title)
    print("duration(secs):",tag.duration)

#test avec des fichiers .mp3 / wav / flac
metadata("file_mp3.mp3")
metadata("file_wav.wav")
metadata("file_flac.flac")