from datetime import datetime

def parse_date(date_str, fmt="%Y-%m-%d"):
    try:
        return datetime.strptime(date_str, fmt).date()
    except ValueError:
        return None

def clean_text(text):
    return text.strip().replace("\n", " ")
