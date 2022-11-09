
![Logo](https://cdn.discordapp.com/attachments/1039608283566178304/1039863790323376188/9042647_ip_address_icon_1.png)


# Discord IP Info Logger 

This is a web based IP info logger which integrates with discord webhooks. You can run it locally or publicly. It will work both ways.


## Features

- Proxy Detection
- Geo Location
- Reverse DNS
- And many more


## Installation




Extremely Easy Set Up
```bash
  chmod +x setup.sh
  ./setup.sh
```

    
## Want it public?

Install ngrok and follow a couple steps.

```bash
    tar -xvzf /path/to/zipfilengrok
    sudo mv ngrok /usr/bin/
    ngrok config add-authtoken <yourtoken>
    ngrok http 9999
```
Make sure your python script is running beforehand for it to work.
Now you have it public to share with anyone. Easy as that.



