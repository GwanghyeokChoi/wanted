
def _company_name_autocomplete(query, x_wanted_language, session, models):
    try:
        if x_wanted_language == "ko":
            column = models.Company.name_ko
        elif x_wanted_language == "en":
            column = models.Company.name_en
        elif x_wanted_language == "ja":
            column = models.Company.name_ja
        elif x_wanted_language == "tw":
            column = models.Company.name_tw

        company = session.query(models.Company).filter(column.ilike(f'%{query}%')).all()

        return companyAutoSearch(company, x_wanted_language)
    except MyError as e:
        return e

def _company_search(company_name, x_wanted_language, session, models):
    try:
        if session.query(models.Company).filter(models.Company.name_ko == company_name).first() is not None:
            column = models.Company.name_ko
        elif session.query(models.Company).filter(models.Company.name_en == company_name).first() is not None:
            column = models.Company.name_en
        elif session.query(models.Company).filter(models.Company.name_ja == company_name).first() is not None:
            column = models.Company.name_ja
        elif session.query(models.Company).filter(models.Company.name_tw == company_name).first() is not None:
            column = models.Company.name_tw

        company = session.query(models.Company).filter(column == company_name).first()

        if company is None:
            return None

        return companyReturn(company, x_wanted_language)
    except MyError as e:
        return e

def _new_company(req_json, x_wanted_language, session, models, service):
    try:
        tag_ko = tag_en = tag_tw = tag_ja = "|"

        company_names = req_json['company_name']
        name_ko = company_names['ko'] if company_names.get('ko') else None
        name_en = company_names['en'] if company_names.get('en') else None
        name_tw = company_names['tw'] if company_names.get('tw') else None
        name_ja = company_names['ja'] if company_names.get('ja') else None
        
        tags = req_json['tags']

        for tag in tags:
            tag_ko = tag_ko + tag['tag_name']['ko'] + "|" if tag['tag_name'].get('ko') else tag_ko
            tag_en = tag_en + tag['tag_name']['en'] + "|" if tag['tag_name'].get('en') else tag_en
            tag_tw = tag_tw + tag['tag_name']['tw'] + "|" if tag['tag_name'].get('tw') else tag_tw
            tag_ja = tag_ja + tag['tag_name']['ja'] + "|" if tag['tag_name'].get('ja') else tag_ja
            
        db_company = models.Company(
            name_ko = name_ko,
            name_en = name_en,
            name_ja = name_ja,
            name_tw = name_tw,
            tag_ko = tag_ko[1:-1],
            tag_en = tag_en[1:-1],
            tag_ja = tag_ja[1:-1],
            tag_tw = tag_tw[1:-1]
        )

        return companyReturn(service.new_Company(session, db_company), x_wanted_language)
    except MyError as e:
        return e

def companyReturn(companyBase, x_wanted_language):
    if x_wanted_language == 'ko':
        name = companyBase.name_ko
        tags = companyBase.tag_ko
    elif x_wanted_language == 'en':
        name = companyBase.name_en
        tags = companyBase.tag_en
    elif x_wanted_language == 'tw':
        name = companyBase.name_tw
        tags = companyBase.tag_tw
    elif x_wanted_language == 'ja':
        name = companyBase.name_ja
        tags = companyBase.tag_ja

    company = {
        "company_name" : name, 
        "tag_name": tags.split("|")
    }

    return company

def companyAutoSearch(companyBase, x_wanted_language):
    company = []
    if x_wanted_language == 'ko':
        for base in companyBase:
            company.append({"company_name": base.name_ko})
    elif x_wanted_language == 'en':
        for base in companyBase:
            company.append({"company_name": base.name_en})
    elif x_wanted_language == 'tw':
        for base in companyBase:
            company.append({"company_name": base.name_tw})
    elif x_wanted_language == 'ja':
        for base in companyBase:
            company.append({"company_name": base.name_ja})
        
    return company