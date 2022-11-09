'''

NOTE - I am not responsible for any use of action with this code. Made only for educational purposes.
AUTHOR - DIARALB
LICENSE - MIT License


'''


from flask import *
from discord_webhook import DiscordWebhook, DiscordEmbed
import re
import time
import requests

app = Flask(__name__)


ipFormat = re.compile(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
urlFormat = re.compile(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')

@app.route("/", methods=["POST", "GET"])
def ipLookup():
	if request.method == "POST":

		ip_address = request.form["ip"]
		dis_webhook = request.form["disc"]

		if ip_address == "" or dis_webhook == "":
			return render_template("iplookup.html")
		else:
			pass

		try:
			ipValidation = ipFormat.search(ip_address.strip())
			ipValidation.group()
		except:
			return render_template("iplookup.html")

		try:
			urlValidation = urlFormat.search(dis_webhook.strip())
			urlValidation.group()
		except:
			return render_template("iplookup.html")


		r = requests.get(f"http://ip-api.com/json/{ip_address}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query")
		ip_data = json.loads(r.text)

		country = ip_data["country"]
		region = ip_data["regionName"]
		city = ip_data["city"]
		latitude = ip_data["lat"]
		longtitude = ip_data["lon"]
		timezone = ip_data["timezone"]
		isp = ip_data["isp"]
		zipcode = ip_data["zip"]
		currency = ip_data["currency"]
		organization = ip_data["org"]
		reverse_lookup = ip_data["reverse"]
		proxy = ip_data["proxy"]


		webhook = DiscordWebhook(url=f'{dis_webhook}', username="IP INFO LOGGER V1", content=f'''''')


		embed = DiscordEmbed(title=f'''IP INFO LOGGED - {ip_address}''', description=f'''



				Target IP --> {ip_address}
			Country - {country}                        
			Region - {region}
			City - {city}
			Latitude - {latitude}
			Longtitude - {longtitude}
			Timezone - {timezone}
			ISP - {isp}
			ZIP - {zipcode}
			Currency - {currency}
			Organization - {organization}
			Reverse DNS - {reverse_lookup}
			IS Proxy - {proxy}




			''', color=3070781)


		embed.set_author(name='DEVELOPER - diaralb', url='https://github.com/Supreme-coder929')

		embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1039608283566178304/1039608437480366140/9042647_ip_address_icon.png')
		embed.set_footer(text="Only for educational purposes.")

		webhook.add_embed(embed)
		webhook.execute()

		return "<script>alert('Data sent to webhook');window.location.replace('http://127.0.0.1:9999');</script>"


		
	else:
		render_template("iplookup.html")

	return render_template("iplookup.html")



if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=9999)