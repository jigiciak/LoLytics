import requests
import os


path_assets = 'http://ddragon.leagueoflegends.com/cdn/12.22.1/data'
api_path_summoner = 'api.riotgames.com/lol/summoner/v4/summoners/by-name'
api_path_matches = 'api.riotgames.com/lol/match/v5/matches/by-puuid'
api_path_single_match = 'api.riotgames.com/lol/match/v5/matches'


def region_parser(platform):
    regions = {"br1": 'americas',
               "eun1": 'europe',
               "euw1": 'europe',
               "jp1": 'asia',
               "kr": 'asia',
               "la1": 'americas',
               "la2": 'americas',
               "na1": 'americas',
               "oc1": 'americas',
               "tr1": 'europe',
               "ru": 'europe'}
    return regions[platform]


def get_champion_info(champion_name):
    return requests.get(f'{path_assets}/en_US/champion/{champion_name}.json').json()['data'][champion_name]


def get_spells_info(champion_info):
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


def get_summoner_info(name, platform):
    player_info = requests.get(f'https://{platform}.{api_path_summoner}/{name}?api_key={os.environ.get("LOL_API_KEY")}').json()
    return player_info


def get_matches(puuid, region):
    matches = requests.get(f'https://{region}.{api_path_matches}/{puuid}/ids?start=0&count=5&api_key={os.environ.get("LOL_API_KEY")}').json()
    return matches


def get_single_match_info(matchid, region):
    match = requests.get(f'https://{region}.{api_path_single_match}/{matchid}?api_key={os.environ.get("LOL_API_KEY")}').json()
    return match


def get_matches_info(matches, region):
    matches_info = []
    for match in matches:
        matches_info.append(get_single_match_info(match, region))
    return matches_info
