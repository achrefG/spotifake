from tinytag import TinyTag
def metadata(filepath):
    tag = TinyTag.get(filepath)

    print("\nartist:", (tag.artist))
    print("album:", tag.album)
    print("title:", tag.title)
    print("duration(secs):",tag.duration)
    print("Musique N°",tag.track)
    print("Compositeur:",tag.composer)
    print("Genre:",tag.genre)
    #print()
    #print(tag) #print all metadata

#test avec des fichiers .mp3 / wav / flac
metadata("Musique/file_mp3.mp3")
#metadata("Musique/file_wav.wav")
#metadata("Musique/file_flac.flac")