#!/usr/bin/env python

# 1. Open a log file, read its content and find all IP address
# 2. Count request from IP
# 3. Write Data to CSV file

import re
import csv
from collections import Counter

# reader function read the log file and display all ip address and return it


def reader(filename):
    with open(filename) as f:
        log = f.read()
        # print(log)

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        # print(ips_log)
        return ips_list

# count function to count the no of times a ip is logged


def count(ips_list):
    counter = Counter(ips_list)
    return counter

# write the counter output to a csv file


def write_csv(counter):
    with open('output.csv', 'w') as myCsv:
        writer = csv.writer(myCsv)

        header = ['IP', 'FREQUENCY']
        writer.writerow(header)

        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == '__main__':
    write_csv(count(reader('access_log')))


