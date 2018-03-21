import requests
import json
import time
import datetime

class siksha():

	@staticmethod
	def get_menu(day=0):
		if day == 0:
			r = requests.get('http://siksha.kr:8230/rate/view?date=today')
			data = json.loads(r.text)
			return data

	@staticmethod
	def get_date_text():
		return time.strftime('%m월 %d일', time.localtime())

	@staticmethod
	def get_meal_now():
		now = datetime.datetime.now()
		if now.hour >= 7 and now.hour < 10:
			return 'breakfast'
		if now.hour >= 10 and now.hour < 14:
			return 'lunch'
		if now.hour >= 14 and now.hour < 19:
			return 'dinner'
		else:
			return ''

	@staticmethod
	def get_type_text(meal_type):
		result = {
			'breakfast': '아침',
			'lunch': '점심',
			'dinner': '저녁'
		}
		try:
			return result[meal_type]
		except KeyError:
			return ''

	@staticmethod
	def format(restaurant, meal_type, foods):
		result = ''
		result += restaurant
		result += '\n'
		result += siksha.get_date_text() + ' '
		result += siksha.get_type_text(meal_type)
		result += '\n'
		for i in foods:
			result += i['name'].replace('(#)', '')
			result += '('
			result += i['price']
			result += '원'
			if 'rating' in i:
				result += ','
				result += str(round(i['rating'], 1))
				result += '점'
			result += ')'
			result += '\n'
		return result
