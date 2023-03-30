from pprint import pprint
from pickle import dump, load
from os.path import exists
from requests import get
from bs4 import BeautifulSoup

from area import get_area_id
from salary import get_salary_range
from skills import get_skills

# ввод интересующей вакансии
# vacancy = input('Введите интересующую вакансию: ')
vacancy = = 'linux'
url = 'https://api.hh.ru/vacancies'

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
rate = data['Valute'] # загрузка текущих курсов валют

# загрузка файла с цифровыми кодами
if exists('area.pkl'):
    with open('area.pkl', mode='rb') as f:
        area = load(f)
else:
    area = {}

p = {'text': vacancy}
r = get(url=url, params=p).json()
count_pages = r['pages']
all_count = len(r['items'])
result = {
        'keywords': vacancy,
        'count': all_count}
sal = {'from': [], 'to': []}
skillis = []

# сначала выявляем сколько будет получено страниц
# и готовим нужные переменные. А затем проходим по каждой из полученных страниц.
for page in range(count_pages):
    if page > 2:
        break
    else:
        print(f"Обрабатывается страница {page}")
    p = {'text': vacancy,
         'page': page}
    ress = get(url=url, params=p).json()
    all_count = len(ress['items'])
    result['count'] += all_count
    
    for res in ress['items']:
        city_vac = res['area']['name']
        # добавление города из ответа на запроса, если его нет в файле.
        if city_vac not in area:
            area[city_vac] = get_area_id(res['area']['id'])
        
        res_full = get(res['url']).json()
        skills = get_skills(res_full['description'], res_full['key_skills'])
        skillis += skills
        
        salary_range = get_salary_range(res_full['salary'], rate)
        sal['from'].append(salary_range['from'])
        sal['to'].append(salary_range['to'])

# формирование результата
result.update({
    'down': round(sum(sal['from']) / len(sal['from']), 2),
    'up': round(sum(sal['to']) / len(sal['to']), 2),
    'requirements': [{'name': name, 'count': count, 'percent': round((count / result['count'])*100, 2)} 
                      for name, count in Counter(skillis).most_common(5)]
})

pprint(result)

# сохранение файла с результами работы
with open('result.json', mode='w') as f:
    jdump([result], f)
with open('area.pkl', mode='wb') as f:
    dump(area, f)
