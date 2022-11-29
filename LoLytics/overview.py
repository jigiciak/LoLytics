from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import requests as rq
from LoLytics.utils import get_info, get_spells
import os


path_assets = os.getenv('PATH_ASSETS')
champions_info = rq.get(f'{path_assets}/en_US/champion.json').json()
champions_list = list(champions_info['data'].keys())
champions_ct = len(champions_list)
champions_names = [champions_info['data'][key]['name'] for key in list(champions_info['data'].keys())]


overview = Blueprint('overview', __name__, template_folder='templates')

@overview.route('/overview', methods=['GET', 'POST'])
def index():
    champion_selected = request.form.get("champion_selected")
    champion_info = get_info('Aatrox')
    lore = champion_info['lore']
    spells= get_spells(champion_info)

    if champion_selected:
        champion_info = get_info(champions_list[champions_names.index(champion_selected)])
        lore = champion_info['lore']
        spells = get_spells(champion_info)
        return render_template('overview.html', champions=champions_list, champions_names=champions_names,
                               champion_selected=champion_selected, lore=lore, spells=spells)
    else:
        return render_template('overview.html', champions=champions_list, champions_names=champions_names,
                               champion_selected=champions_list[0], lore=lore, spells=spells)

