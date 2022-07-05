import json
import pymongo
import os
import glob
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("Your-MongoDB-URL")
mydb = myclient["bdates"]
mycol = mydb["new_data"]

while True:
	lst = []
	x = mycol.find_one({"_id": ObjectId("61806436528d19b2e1062090")}, {"_id":0,"new":1})
	print(x)
	
	if x["new"] == "1":
		mycol1 = mydb["users"]
		for y in mycol1.find({},{"_id":0,"name":1,"insta_id":1,"date":1,"month":1}):
			lst.append(y)
		
		print(lst)
		
		# os.system("rm data.json")
		os.system("del data.json")
		with open('data.json', 'w') as f:
			json.dump(lst, f, indent=4)
		

		myquery = { "_id": ObjectId("61806436528d19b2e1062090") }
		newvalues = { "$set": { "new" : "0" } }
		mycol.update_one(myquery, newvalues)