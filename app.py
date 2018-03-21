import twitter
import configs

api = twitter.Api(consumer_key=configs.apikey,
	consumer_secret=configs.secret,
	access_token_key=configs.token,
	access_token_secret=configs.token_secret)

import siksha
import datetime

menu = siksha.siksha.get_menu()
meal_now = siksha.siksha.get_meal_now()


now = datetime.datetime.now()
if now.hour in configs.post_time:

	for i in menu['data']:
		restaurant = i['restaurant']
		foods = i['foods']

		foods_now = list(filter(lambda x: x['time'] == meal_now, foods))
		if len(foods_now) > 0:
			result = siksha.siksha.format(restaurant, meal_now, foods_now)
			api.PostUpdate(result)