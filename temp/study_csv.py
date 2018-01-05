'''
http://blog.csdn.net/u011284860/article/details/51031051
'''

import csv


def write_csv(name='data/some.csv'):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['a', '1', 'c'])
    pass


def write_csv_delimiter(name='data/some.csv'):
    with open(name, 'w') as f:
        writer = csv.writer(f, delimiter=":", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['a', '1', 'c'])
    pass


def reader_csv(name='data/some.csv'):
    with open(name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    pass


def reader_csv_delimiter(name='data/some.csv'):
    with open(name, 'r') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row)
    pass



if __name__ == '__main__':

    reader_csv_delimiter()

    pass