#! python3
# umbrellaReminder.py - Weather API that sends me text messages

from twilio.rest import Client
import requests, bs4


# rest API from twilio
# Your Account SID from twilio.com/console
account_sid = "AC7226356ef66d2de53d535237cba9e2dc"
# Your Auth Token from twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


myNumber = '+1469XXXXXXX'
client = Client(account_sid, auth_token)

# create a message to myself
def textmyself():


	res = requests.get('https://weather.com/weather/today/l/c1535f42ba5fc52449e416514aca69b3b2a16aae4b89abd6c92e662f7a89c02f').text
	soup = bs4.BeautifulSoup(res, features='html.parser')

	state = soup.find('header', class_='loc-container').text
	fullforcast = soup.find('div', class_='today_nowcard-section today_nowcard-condition').text
	

	message = client.messages.create(
	    to="+14695104352", 
	    from_="+17033489722",
	    body= fullforcast)

	return message.sid 

#print(textmyself())



#print(weather.prettify())

