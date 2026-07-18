def is_number(text: str) -> bool:
    try:
        float(text)
        return True
    except Exception:
        return False
