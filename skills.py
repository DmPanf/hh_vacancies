import re

def get_skills(description, key_skills):
    pp = BeautifulSoup(description, features="html.parser").get_text()
    pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
    its = set(x.strip(' -').lower() for x in pp_re)
    
    skills = set()
    for sk in key_skills:
        skills.add(sk['name'].lower())
        
    for it in its:
        if not any(it in x for x in skills):
            skills.add(it)
            
    return list(skills)
