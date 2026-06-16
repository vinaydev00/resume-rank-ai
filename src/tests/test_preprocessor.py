from src.preprocessor import TextPreprocessor

def test_removes_email():
    p = TextPreprocessor()
    result = p.remove_personal_info("Contact me at john@example.com")
    assert "john@example.com" not in result
    assert "[EMAIL]" in result

def test_removes_phone():
    p = TextPreprocessor()
    result = p.remove_personal_info("Call me at 9876543210")
    assert "9876543210" not in result

def test_clean_whitespace():
    p = TextPreprocessor()
    result = p.clean("Hello    World   ")
    assert "  " not in result

def test_normalize_titles():
    p = TextPreprocessor()
    result = p.normalize_titles("Sr. Software Eng")
    assert "Senior" in result