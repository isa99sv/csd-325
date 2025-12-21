# Colton Stone, December 20, 2025, Module 12.2 Assignment

def get_location(city, country, population='', language=''):
    if language:
        set_location = city + ' ' + country + ' ' + population + ' ' + language
    elif population:
        set_location = city + ' ' + country + ' ' + population
    else:
        set_location = city + ' ' + country
    return set_location

get_location('Paris', 'France', '5000', 'French')
get_location('London', 'England', '7000')
get_location('Tokyo', 'Japan')

