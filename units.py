import re


def get_unit(multiplier):
    """Returns a string with proper metric prefix"""
    regex = re.compile(r'[A-Za-z]')
    multiplier = int(regex.sub('', multiplier))

    if multiplier <-6:
        unit = 'nV'
    elif -6 <= multiplier < -3:
        unit = 'uV'
    elif -3 <= multiplier < 0:
        unit = 'mV'
    elif 0 <= multiplier < 3:
        unit = 'V'
    elif 3 <= multiplier < 6:
        unit = 'kV'
    else:
        unit = "Out of range"

    return unit
