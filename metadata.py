from tinytag import TinyTag
from PIL import Image
import io
def metadata(filepath):
    tag = TinyTag.get(filepath,image=True)


    print("\nartist: ", (tag.artist))
    print("album: ", tag.album)
    print("title: ", tag.title)
    print("duration(secs): ",tag.duration)
    print("Musique N° ",tag.track)
    print("Compositeur:",tag.composer)
    print("Genre: "+str(tag.genre)+" \n")
    return tag
    img = tag.get_image()
    #print(img,"\n\n\n")


    if(img != None):
        pi = Image.open(io.BytesIO(img))
        pi.show()
    #Make a PIL Image


    #print("")
    #print(tag) #print all metadata



'''--------------------------------------- TEST -------------------------------'''


#metadata("Musique/damso.mp3")
#test avec des fichiers .mp3 / wav / flac
#metadata("Musique/test.mp3")
#metadata("Musique/test.flac")
