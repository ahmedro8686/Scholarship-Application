from scraper.parser import parse_date, clean_text
from datetime import date

def test_parse_date():
    assert parse_date("2025-08-14") == date(2025, 8, 14)
    assert parse_date("invalid") is None

def test_clean_text():
    assert clean_text(" hello \n") == "hello"
