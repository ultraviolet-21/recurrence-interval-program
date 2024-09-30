#filter_options.py
#Allows user to filter a list of intervals

def get_most_recent(data: list[int], fraction: float) -> list[int]:
    '''Only recent data'''
    section = round(len(data) * fraction)
    return data[len(data)-section::]

def greater_than_or_equal(data: list[int], x: int | float) -> list[int]:
    '''Filters out low outliers'''
    return list(filter(lambda n: n >= x, data))

def less_than_or_equal(data: list[int], x: int | float) -> list[int]:
    '''Filters out high outliers'''
    return list(filter(lambda n: n <= x, data))

def options(data: list[int]) -> list[int]:
    '''Allows user to decide if they want to filter the list, returns unchanged list otherwise'''
    print('Option 1: get most recent fraction of data')
    print('Option 2: get data over a certain value')
    print('Option 3: get data under a certain value')
    print('Option 4: keep unchanged')
    option = input('Select 1, 2, 3, or 4: ')
    if option == '1':
        value = input('fraction: ')
        return get_most_recent(data, float(value))
    elif option == '2':
        value = input('value: ')
        return greater_than_or_equal(data, float(value))
    elif option == '3':
        value = input('value: ')
        return less_than_or_equal(data, float(value))
    else:
        return data
