from flask import Flask, render_template, request
import requests as rq

app = Flask(__name__)
region = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR',
          'LA1', 'LA2', 'NA1', 'OC1', 'TR1',
          'RU']
path_api = f'https://{region[1]}.api.riotgames.com/'
path_assets = 'http://ddragon.leagueoflegends.com/cdn/12.22.1/data'
champions_info = rq.get(f'{path_assets}/en_US/champion.json').json()
champions_list = list(champions_info['data'].keys())
champions_ct = len(champions_list)
champions_names = [champions_info['data'][key]['name'] for key in list(champions_info['data'].keys())]


def get_info(champion_name):
    return rq.get(f'{path_assets}/en_US/champion/{champion_name}.json').json()['data'][champion_name]


def get_spells(champion_info):
    spells_icons = [champion_info['passive']['image']['full'],
                    champion_info['spells'][0]['image']['full'],
                    champion_info['spells'][1]['image']['full'],
                    champion_info['spells'][2]['image']['full'],
                    champion_info['spells'][3]['image']['full']]

    spells_names = [champion_info['passive']['name'],
                    champion_info['spells'][0]['name'],
                    champion_info['spells'][1]['name'],
                    champion_info['spells'][2]['name'],
                    champion_info['spells'][3]['name']]

    spells_descriptions = [champion_info['passive']['description'],
                           champion_info['spells'][0]['description'],
                           champion_info['spells'][1]['description'],
                           champion_info['spells'][2]['description'],
                           champion_info['spells'][3]['description']]

    return [spells_icons, spells_names, spells_descriptions]


@app.route('/', methods=['GET', 'POST'])
def index():
    champion_selected = request.form.get("champion_selected")
    champion_info = get_info('Aatrox')
    lore = champion_info['lore']
    spells= get_spells(champion_info)

    if champion_selected:
        champion_info = get_info(champions_list[champions_names.index(champion_selected)])
        lore = champion_info['lore']
        spells = get_spells(champion_info)
        return render_template('index.html', champions=champions_list, champions_names=champions_names,
                               champion_selected=champion_selected, lore=lore, spells=spells)
    else:
        return render_template('index.html', champions=champions_list, champions_names=champions_names,
                               champion_selected=champions_list[0], lore=lore, spells=spells)

