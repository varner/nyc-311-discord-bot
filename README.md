# NYC 311 Discord Bot

This script lets you automatically notify a Discord channel about new 311 calls for a specified address.

## Installation

To run locally, `pip install requirements.txt`. You'll need to set the config vars, as outlined below, in an `.env` file for it to work.

I run this software for free on [Heroku](https://dashboard.heroku.com/). If you're doing this as well:

1. Provision [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler). 
2. Set a job for every ten minutes with the command `python3 run.py`
3. Add the following config vars:
	- `ADDRESS` : `YOUR_STREET_ADDRESS_HERE`
	- `ZIPCODE` : `YOUR_ZIPCODE_HERE`
	- `INTERVAL` : `10`
	- `DISCORD_URL`: `DISCORD_WEBHOOK_URL_HERE`
	- `TZ` : `America/New_York`

## License

this code is licensed under [the fuck around and find out license v0.1](https://paste.sr.ht/~boringcactus/ed023ccf9d7a5559612d6e60f0474d6c3375349d).

copyright (c) 2021 Maddy Varner

permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "software"), to deal in the software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, and to permit persons to whom the software is furnished to do so, subject to the following conditions:

the above copyright notice and this permission notice shall be included in all copies or substantial portions of the software.

the software shall be used for Good, not Evil. the original author of the software retains the sole and exclusive right to determine which uses are Good and which uses are Evil.

the software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. in no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.