#interval_calc
#Handles all calculations regarding recurrence intervals and final probability

from onevar_stats import *
from datetime import datetime
from pathlib import Path
import distribution
import lognorm
from filter_options import options

def read_from_file(file_path: Path) -> list[int]:
    '''Reads time-series data from a file, assuming correct format'''
    try:
        with open(file_path, 'r') as the_file:
            try:
                for line in the_file:
                    yield int(line.strip())
            except:
                print('Data not in time-series format')
    except:
        print('File not found')

def get_intervals(years: list[int]):
    '''Returns a list of the intervals between data points'''
    for x in range(len(years) - 1):
        yield years[x] - years[x+1]

if __name__ == '__main__':
    file_path = Path(input('Enter a file path: '))
    years = list(read_from_file(file_path))
    ref_point = int(input('Enter a reference point: '))
    intervals = list(get_intervals(years))
    intervals = options(intervals)
    mu = mean(intervals)
    sigma = stdev(intervals)
    start = int(input('Enter a start point: '))
    end = int(input('Enter an end point: '))
    print(lognorm.probability(ref_point, start, end, mu, sigma))
    distribution.make_kde(intervals)


