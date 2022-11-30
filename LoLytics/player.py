from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import requests as rq
from LoLytics.utils import get_champion_info, get_spells_info, get_summoner_info, get_matches, region_parser, get_single_match_info
import json
import os


player_bp = Blueprint('player', __name__, template_folder='templates')
api_key = os.environ.get("LOL_API_KEY")
platform = json.loads(os.environ.get("PLATFORMS"))[1]

path_assets = "http://ddragon.leagueoflegends.com/cdn/12.22.1/data"
champions_info = rq.get(f'{path_assets}/en_US/champion.json').json()
champions_list = list(champions_info['data'].keys())
champions_names = [champions_info['data'][key]['name'] for key in list(champions_info['data'].keys())]

@player_bp.route('/player', methods=['GET', 'POST'])
def player():
    try:
        player_name = request.form.get("summoners_name")
        match_id = request.form.get("match_id")
        if player_name:
            summoner_info = get_summoner_info(player_name, 'eun1')
            matches = get_matches(summoner_info['puuid'], region_parser('eun1'))
            if match_id:
                single_match_info = get_single_match_info(match_id, region_parser('eun1'))
            else:
                single_match_info = get_single_match_info(matches[0], region_parser('eun1'))
            summoners = [summoner for summoner in single_match_info['info']['participants']]
            s_names = [summoner['summonerName'] for summoner in summoners]
            s_champions = [summoner['championName'] for summoner in summoners]
            s_champions_n = [champions_names[champions_list.index(champ)] for champ in s_champions]
            s_kills = [summoner['kills'] for summoner in summoners]
            s_deaths = [summoner['deaths'] for summoner in summoners]
            s_assists = [summoner['assists'] for summoner in summoners]
            return render_template('player.html', player_name=player_name, match_id=None, summoners_name=s_names,
                                   champions=s_champions, champion_names=s_champions_n)
        else:
            return render_template('index.html')
    except TemplateNotFound:
        abort(404)

# http://ddragon.leagueoflegends.com/cdn/12.22.1/img/champion/Aatrox.png
# "championId": 161,
# "championName": "Velkoz",