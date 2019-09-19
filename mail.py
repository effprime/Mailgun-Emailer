from requests import post as http_post
from json import load as json_load
from datetime import datetime as right

def send_login_alert(
    api_url, 
    api_key, 
    from_addr, 
    to_addr,
    subject,
    message,
    time
):
	return http_post(
		api_url,
		auth=("api", api_key),
		data={
            "from": from_addr, 
            "to": to_addr, 
            "subject": subject,
            "text": message + "\n\n" + "Time: %s" % (time)
        }
    )

with open("data.json","r") as file:
    args = json_load(file)
args["time"] = right.now()
send_login_alert(**args)