#!/usr/bin/env python

import re
from collections import Counter

regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
try:
    def reader(filename):
        with open(filename) as f:
            print("Reading Apache Log File")
            Apache_log = f.read()
            get_ip = re.findall(regex,Apache_log)
            # print(get_ip)
            return get_ip
except:
    print("file not found")            

def count(get_ip):
    counter = Counter(get_ip)
    # print(counter)
    return counter

def report(counter):
    for item in counter:
        print ("Available IP Address " + " =>" + item + " -- Count => " + str(counter[item]))   
if __name__ == '__main__':
    try:
        report(count(reader('access_log')))
    except:
        print("file not found")    