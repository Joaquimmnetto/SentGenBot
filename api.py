import requests
import json


def api_request(token, method, args):

	r = requests.post('https://api.telegram.org/bot{0}/{1}'.format(token, method), json=args)

	if r.status_code != 200:
		print("Request failed with a ", r.status_code)
		return False

	resp = json.loads(r.text)

	return resp