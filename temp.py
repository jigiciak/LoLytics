from flask import Flask, render_template, request, render_template_string
import requests as rq
import json

app = Flask(__name__)
region = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR',
          'LA1', 'LA2', 'NA1', 'OC1', 'TR1',
          'RU']
path_api = f'https://{region[1]}.api.riotgames.com/'
champions_info = rq.get('http://ddragon.leagueoflegends.com/cdn/12.22.1/data/en_US/champion.json').json()
champions_list = list(champions_info['data'].keys())
champions_ct = len(champions_list)
champions_names = [champions_info['data'][key]['name'] for key in list(champions_info['data'].keys())]


# print('args:', request.args)
# print('form:', request.form)
temp = rq.get(f'http://ddragon.leagueoflegends.com/cdn/12.22.1/data/en_US/champion/Kayn.json').json()['data']['Kayn']

print(temp.keys())
print(json.dumps([temp['passive']], indent=4))
# print(json.dumps([temp['passive']], indent=4))
# print(temp['spells'][0]['image']['full'])
