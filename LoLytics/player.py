from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import requests as rq
from LoLytics.utils import get_champion_info, get_spells_info, get_summoner_info, get_matches, region_parser, get_single_match_info
import json
import os


player_bp = Blueprint('player', __name__, template_folder='templates')
api_key = os.environ.get("LOL_API_KEY")
platform = json.loads(os.environ.get("PLATFORMS"))[1]
player_name = "Tamiko"

path_assets = "http://ddragon.leagueoflegends.com/cdn/12.22.1/data"
champions_info = rq.get(f'{path_assets}/en_US/champion.json').json()

@player_bp.route('/player', methods=['GET', 'POST'])
def player():
    try:
        player_name = request.form.get("summoners_name")
        print(player_name)
        if player_name:
            summoner_info = get_summoner_info(player_name, 'eun1')
            matches = get_matches(summoner_info['puuid'], region_parser('eun1'))
            single_match_info = get_single_match_info(matches[0], region_parser('eun1'))
            summoners = [summoner['summonerName'] for summoner in single_match_info['info']['participants']]
            champions = [champion['championName'] for champion in single_match_info['info']['participants']]
            return render_template('player.html', player_name=player_name, summoners_name=summoners, champions=champions)
        else:
            return render_template('player.html', player_name=None, summoners_name=None, champions=None)
    except TemplateNotFound:
        abort(404)

# http://ddragon.leagueoflegends.com/cdn/12.22.1/img/champion/Aatrox.png
# "championId": 161,
# "championName": "Velkoz",