from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import requests as rq
from LoLytics.utils import get_champion_info, get_spells_info
import os


overview_bp = Blueprint('overview', __name__, template_folder='templates')

path_assets = "http://ddragon.leagueoflegends.com/cdn/12.22.1/data"
champions_info = rq.get(f'{path_assets}/en_US/champion.json').json()
champions_list = list(champions_info['data'].keys())
champions_ct = len(champions_list)
champions_names = [champions_info['data'][key]['name'] for key in list(champions_info['data'].keys())]


def populate_overview(champion_selected, champ_list):
    if not champion_selected:
        champion_selected = champ_list[0]
    champion_info = get_champion_info(champion_selected)
    lore = champion_info['lore']
    spells = get_spells_info(champion_info)

    return lore, spells


@overview_bp.route('/overview', methods=['GET', 'POST'])
def overview():
    try:
        champion_selected = request.form.get("champion_selected")
        lore, spells = populate_overview(champion_selected, champions_list)
        if champion_selected:
            return render_template('overview.html', champions=champions_list, champions_names=champions_names,
                                   champion_selected=champion_selected, lore=lore, spells=spells)
        else:
            return render_template('overview.html', champions=champions_list, champions_names=champions_names,
                                   champion_selected=champions_list[0], lore=lore, spells=spells)
    except TemplateNotFound:
        abort(404)