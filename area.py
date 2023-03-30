from pickle import dump, load
from os.path import exists
from requests import get

def get_area_id(area_id):
    # загрузка файла с цифровыми кодами
    if exists('area.pkl'):
        with open('area.pkl', mode='rb') as f:
            area = load(f)
    else:
        area = {}
    
    if area_id in area.values():
        return area_id
    
    url = f'https://api.hh.ru/areas/{area_id}'
    res = get(url=url).json()
    area[res['name']] = res['id']
    
    # сохранение файла с результами работы
    with open('area.pkl', mode='wb') as f:
        dump(area, f)
    
    return res['id']
