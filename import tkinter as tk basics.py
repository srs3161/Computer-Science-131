from tkinter import *
#from PIL import Image, ImageTk
navraj_root= Tk()
navraj_root.geometry("600x600")
#navraj_root.minsize(100,200)
#navraj_root.maxsize(1200,1200)
navraj_root.title("Navraj Photo")
#navraj = Label(text="Navraj is a good programmer")
#image = Image.open("D:/satyendra.jpg")
#photo =ImageTk.PhotoImage(image)
#satyendra_label = Label(image=photo)
#satyendra_label.pack()
#navraj_label = Label(text=''' 
#Virat Kohli (Hindi pronunciation: [ʋɪˈɾɑːʈ ˈkoːɦli] ⓘ; born 5 November 1988) is an Indian international cricketer and\n the former captain of the Indian national cricket team. 
#\nHe currently represents Royal Challengers Bangalore in the IPL and Delhi in domestic cricket.
#\nKohli is widely regarded as one of the greatest batsmen in the history of the sport.
#\nHe is the highest run scorer in T20I and IPL. 
#\nIn 2020, the International Cricket Council named him the male cricketer of the decade.
#\nKohli is currently fourth-highest run-scorer in international cricket and stands second in the list of most international centuries scored. 
#\nHe also holds the record for scoring the most centuries in One Day International cricket.
#\nKohli was a member of the Indian team that won the 2011 Cricket World Cup and 2013 ICC Champions Trophy.''', bg="yellow", fg="white", padx=34, pady=94, font="Arial 14 bold", borderwidth=3,relief=SUNKEN)
#navraj_label.pack(anchor="nw")
f1 = Frame(navraj_root, bg="red", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y", pady=122)
f2 = Frame(navraj_root, borderwidth=9, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l= Label(f1, text="131-student pdf")
l.pack(pady=142)

navraj_root.mainloop()