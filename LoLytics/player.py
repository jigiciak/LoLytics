from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import requests as rq
from LoLytics.utils import get_champion_info, get_spells_info, get_summoner_info, get_matches, region_parser
import json
import os


player_bp = Blueprint('player', __name__, template_folder='templates')
api_key = os.environ.get("LOL_API_KEY")
platform = json.loads(os.environ.get("PLATFORMS"))[1]
player_name = "Tamiko"

###
summoner_info = get_summoner_info('Tamiko', 'eun1')
print(summoner_info)
matches = get_matches(summoner_info['puuid'], region_parser('eun1'))
print(matches)
###

@player_bp.route('/player', methods=['GET', 'POST'])
def player():
    # print(player_info)
    pass