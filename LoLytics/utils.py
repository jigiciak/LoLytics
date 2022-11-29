import requests
import os


path_assets = os.getenv('PATH_ASSETS')


def get_info(champion_name):
    return requests.get(f'{path_assets}/en_US/champion/{champion_name}.json').json()['data'][champion_name]


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