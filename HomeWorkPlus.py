def format_large_number(number):
    if number == 0:
        return '0'

    abbreviations = [
        (1e30, 'dr'),
        (1e27, 'aa'), (1e24, 'ad'), (1e21, 'ac'),
        (1e18, 'ab'), (1e15, 'aa'), (1e12, 'T'),
        (1e9, 'B'), (1e6, 'M'), (1e3, 'K'),
    ]

    for value, notation in abbreviations:
        if abs(number) >= value:
            result = round(number / value, 2)
            return f'{int(result) if result.is_integer() else result}{notation}'

    return '0'
num = float(input(''))
print(format_large_number(num))