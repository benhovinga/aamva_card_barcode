def trim_to_indicator(_str: str, indicator: str) -> str:
    """Remove everything before the indicator, moving the indicator to the begining of the string"""
    if _str[0] != indicator:
        try:
            index = _str.index(indicator)
        except ValueError:
            raise ValueError(f"Indicator \"{indicator}\" is missing")
        _str = _str[index:]
    return _str