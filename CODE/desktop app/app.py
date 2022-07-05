from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("Your-MongoDB-URL")
mydb = myclient["bdates"]
mycol = mydb["new_data"]
mycol1 = mydb["users"]



window = Tk()
window.iconbitmap('instabot.ico')
window.title("B'day Wisher")
window.geometry("320x170")
window.minsize(width=320, height=300)
window.maxsize(width=320, height=300)
window.config(background = "black")








def add_data():
	global name,ig_id,date,month

	n = name.get(1.0, "end-1c")
	i = ig_id.get(1.0, "end-1c")
	d = date.get(1.0, "end-1c")
	m = month.get(1.0, "end-1c")

	print(n)
	print(i)
	print(d)
	print(m)

	mydict = { "name": n,"insta_id": i,"date": d,"month": m }
	x = mycol1.insert_one(mydict)

	myquery = { "_id": ObjectId("61806436528d19b2e1062090") }
	newvalues = { "$set": { "new" : "1" } }
	mycol.update_one(myquery, newvalues)



lb_name = Label(window, text = "Name :").place(x=0 , y=-120 ,relx = 0.2, rely = 0.5, anchor = CENTER)
name = Text(window,height=1,width=15)
name.place(x=0 , y=-120 ,relx = 0.5, rely = 0.5, anchor = CENTER)

lb_ig_id = Label(window, text = "Insagram :").place(x=0 , y=-90 ,relx = 0.175, rely = 0.5, anchor = CENTER)
ig_id = Text(window,height=1,width=15)
ig_id.place(x=0 , y=-90 ,relx = 0.5, rely = 0.5, anchor = CENTER)

lb_date = Label(window, text = "Date :").place(x=0 , y=-60 ,relx = 0.2, rely = 0.5, anchor = CENTER)
date = Text(window,height=1,width=15)
date.place(x=0 , y=-60 ,relx = 0.5, rely = 0.5, anchor = CENTER)

lb_month = Label(window, text = "Month :").place(x=0 , y=-30 ,relx = 0.2, rely = 0.5, anchor = CENTER)
month = Text(window,height=1,width=15)
month.place(x=0 , y=-30 ,relx = 0.5, rely = 0.5, anchor = CENTER)


button_slt = Button(window,text = "Add",command = add_data)
button_slt.place(x=0 , y=10 ,relx = 0.5, rely = 0.5, anchor = CENTER)

window.mainloop()
