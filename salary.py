def get_salary_range(salary_info, rate):
    if not salary_info:
        return {'from': None, 'to': None}
    
    code = salary_info['currency']
    if rate[code] == '':
        code = 'RUR'
    
    k = 1 if code == 'RUR' else float(rate[code]['Valute'])
    
    return {
        'from': k * salary_info['from'] if salary_info['from'] else None,
        'to': k * salary_info['to'] if salary_info['to'] else None
    }
