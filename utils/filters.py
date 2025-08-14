def filter_by_level(scholarships, level):
    return [s for s in scholarships if s.level.lower() == level.lower()]

def filter_by_country(scholarships, country):
    return [s for s in scholarships if s.country.lower() == country.lower()]

def filter_by_deadline(scholarships, before_date):
    return [s for s in scholarships if s.deadline and s.deadline <= before_date]
