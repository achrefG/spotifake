from tinytag import TinyTag
fpath = 'Bad_Habits.mp3'
tag = TinyTag.get(fpath)
print()
print("artist", (tag.artist))
print("album:", tag.album)
print("title:", tag.title)
print("duration(secs):",tag.duration)