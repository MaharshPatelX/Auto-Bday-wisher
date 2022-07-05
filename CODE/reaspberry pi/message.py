from instabot import Bot
import json
from datetime import date
import time
bot = Bot()

bot.login(username="user", password="pass", use_cookie = False)


old_d = date.today().strftime("%d/%m/%Y")
flg = 0

while True:
	new_d = date.today().strftime("%d/%m/%Y")
	date_ = date.today().strftime("%d")
	month_ = date.today().strftime("%m")

	if new_d == old_d:
		if flg == 0:
			print("flg is 0")
			try:
				with open("data.json") as json_file:
					data = json.load(json_file)
			except:
				time.sleep(20)
				with open("data.json") as json_file:
					data = json.load(json_file)

			today_data = []
			
			for d in data:
				if d["date"] == date_:
					if d["month"] == month_:
						today_data.append(d["insta_id"])
			name_s = "Happy Birthday 🍰"

			for td in today_data:
				bot.send_message(name_s, td)
				print(td)
			
			flg = 1

	else:
		print("date not matched")
		old_d = date.today().strftime("%d/%m/%Y")
		flg = 0

	print("next")


	time.sleep(240)
