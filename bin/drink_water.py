import time
import json
from win10toast import ToastNotifier
notifier = ToastNotifier()

file = open("drink_water_settings.json", 'r')
content = file.read()
json_data = json.loads(content)
# print(json_data)
remind_minutes = int(json_data["Remind_minutes"])
remind_seconds = int(json_data["Remind_seconds"])
remind_time = remind_minutes * 60 + remind_seconds
message = str(json_data["Message"])
i = 0
while i < remind_time:
	i += 1
	time.sleep(1)
	if i == remind_time - 1:
	    notifier.show_toast("Time to Drink Water", message, icon_path="icon.ico", duration=10, threaded=True)
	    i = 0
