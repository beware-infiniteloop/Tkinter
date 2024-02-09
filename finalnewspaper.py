from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("700x700")
root.minsize(100,100)
root.title("THE DAILY PROPHET")


# HEADER
head=Frame(root,bg="yellow", bd=4,width=100,height=200 )
head.pack(fill="both", anchor='n')
title=Label(head,text="THE DAILY PROPHET", font=("Times New Roman",40,"bold"),bg="yellow",)
title.pack()


# NEWS 1
N1=Frame(root,bg="brown", bd=10, relief=SOLID, borderwidth=5)
N1.pack(fill=X,anchor='ne')
n1_heading = Label(N1, text="DUMBLEDORE IN TROUBLE", font=("Times New Roman", 25, "bold"), bg="brown", fg="black")
n1_heading.pack(side=TOP,anchor="center")
pic=Image.open(r"C:\Users\Arup Bhattacharjee\Downloads\hp1.jpg")
img=ImageTk.PhotoImage(pic)
img_label=Label(N1,image=img)
img_label.pack(side=LEFT)
n1_text=Label(N1, text='''Christmas Eve is a big day for the western world – for both Wizard, Witch and Muggle alike. This \nChristmas Eve a performer of the magical arts, also known as a “magician” to muggles, by the name of Ryland Silverthorne has \ncaught the attention of The Department of Magical Accidents and Catastrophes for revealing how one of his famous tricks is \npreformed. The “Trick” in question breaks The Statue of Secrecy (instituted in 1689) and consists of a standard disappearing \nact in which Silverhtorne has a volunteer from the audience join him on stage. After choosing his audience selected assistant \nhe then apparates with the chosen muggle to the back of the room behind the spectators, in plain view for everyone to see.''',bg="brown",font=("Times New Roman",10))
n1_text.pack(side=LEFT)

# NEWS2
N2=Frame(root,bg="brown", bd=10, relief=SOLID, borderwidth=1)
N2.pack(fill=X,anchor='ne')
n2_heading = Label(N2, text="THE DARK LORD RISES", font=("Times New Roman", 25, "bold"), bg="brown", fg="black")
n2_heading.pack(side=TOP,anchor="center")
pic2=Image.open(r"C:\Users\Arup Bhattacharjee\Downloads\hp3.jpg")
img2=ImageTk.PhotoImage(pic2)
img_label2=Label(N2,image=img2)
img_label2.pack(side=LEFT,anchor='nw')
n2_text=Label(N2, text='''The Wizarding World has been thrown into a state of shock and awe with the sensational revelation \nthat memories of the notorious Lord Voldemort have been discovered. This news has ignited a wildfire of emotions among wizards \nand witches, with some reacting with excitement and curiosity, while others are gripped by fear and trepidation. Many in the \nWizarding World are keen to delve into the enigmatic mind of the Dark Wizard, eager to unravel the mysteries surrounding his \nrise to power and the motives behind his malevolent deeds. However, there are those who are deeply concerned about what these \nmemories might reveal. Could they contain secrets of dark spells and curses that could be used to inflict harm on others? \nMight they disclose the locations of additional Horcruxes or other potent hidden artifacts?''',bg="brown",font=("Times New Roman",10))
n2_text.pack(side=LEFT)

# NEWS3
N3=Frame(root,bg="brown", bd=10, relief=SOLID, borderwidth=5)
N3.pack(fill=X,anchor='ne')
n3_heading = Label(N3, text="WHO WILL TRIUMPH? SNAPE OR ALBUS", font=("Times New Roman", 25, "bold"), bg="brown", fg="black")
n3_heading.pack(side=TOP,anchor="center")
pic3=Image.open(r"C:\Users\Arup Bhattacharjee\Downloads\hp2.jpg")
img3=ImageTk.PhotoImage(pic3)
img_label3=Label(N3,image=img3)
img_label3.pack(side=LEFT)
n3_text=Label(N3, text='''One memory, in particular, has proven to be quite revelatory. It transported the investigators back \nto a time when a young Tom Riddle was a student at Hogwarts School. The memory showed Riddle seated \nin the imposing Headmaster’s office, under the watchful gaze of none other than Albus Dumbledore himself. \n“Tom, I have reason to believe that you have been practicing Dark magic,” \nDumbledore said gravely, his blue eyes never leaving the young man’s face.Riddle’s expression remained stoic. \n”In that instant, Riddle’s calm façade shattered, revealing a flicker of rage. “I have no idea how that got there,” he hissed. ''',bg="brown", font=("Times New Roman",10))
n3_text.pack(side=LEFT)

# Close Button
close_button = Button(head, text="Close", command=root.destroy, font=("Times New Roman", 10))
close_button.pack(side=BOTTOM, anchor='ne')

root.mainloop()