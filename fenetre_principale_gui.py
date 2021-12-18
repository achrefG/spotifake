import tkinter
from tkinter import  Canvas, Label, PhotoImage, ttk
from tkinter import font
from tkinter.constants import  CENTER, FALSE, LEFT, SUNKEN,BOTTOM, Y, YES

from GUI import main_menu

app_principale=tkinter.Tk()
app_principale.title("SPOTIFAKE")

#CENTRER LA FENETRE
lar_ecran= int(app_principale.winfo_screenwidth())
haut_ecran=int(app_principale.winfo_screenheight())
lar_fen= 600
haut_fen=600

pos_x= (lar_ecran//2)-(lar_fen//2)
pos_y= (haut_ecran//2)-(haut_fen//2)

geo="{}x{}+{}+{}".format(lar_fen,haut_fen,pos_x,pos_y)
app_principale.geometry(geo) # prend en string la longueurxhauteur+positionX+positionY
app_principale.minsize(600,600)
app_principale.resizable(width=FALSE, height=FALSE)

background_color='#000000'
app_principale.config(background=background_color)
app_principale.iconbitmap("Picture\Spotify.ico")


#frame_bouton= tkinter.Frame(app_principale,bg=background_color)#, bd=1 , relief=SUNKEN

label_titre=Label(app_principale, text="SPOTIFAKE",font=('Stencil',40), bg=background_color,fg="#FFFFFF")
label_titre.pack(pady=20)


'''image_spotify= PhotoImage("code\Picture\lama.png")
canvas_image_spotify=Canvas(app_principale,width=500, height=300)
canvas_image_spotify.create_image(10,10,image=image_spotify)

canvas_image_spotify.pack(expand=YES)'''


boutton_lancer=tkinter.Button(app_principale, text="LANCER" , font=('Stencil',20) , width=8,command=main_menu )
boutton_quitter=tkinter.Button(app_principale, text="QUITTER", font=('Stencil',20), width=8,command=app_principale.quit)

boutton_quitter.pack(pady=20,side=BOTTOM)
boutton_lancer.pack(side=BOTTOM)


#frame_bouton.pack(pady=25)




app_principale.mainloop()
