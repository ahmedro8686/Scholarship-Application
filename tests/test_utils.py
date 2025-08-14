from utils.validator import is_valid_email, is_non_empty_string

def test_email_validator():
    assert is_valid_email("test@example.com")
    assert not is_valid_email("invalid-email")

def test_non_empty_string():
    assert is_non_empty_string("hello")
    assert not is_non_empty_string("   ")
