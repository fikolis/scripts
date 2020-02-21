#!/usr/bin/python3

import os
import re
import argparse

parser = argparse.ArgumentParser(
    description='This script reads log file parsing, file extensions, and count t them.')
parser.add_argument(
    "-f", "--file", help="enter full path of log file", required=True)
args = parser.parse_args()

print("""

 ____ ____ ____ ____ ____ ____ ____
||L |||o |||g |||R |||e |||a |||d ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|


                    """)

if os.path.isfile(args.file):
    with open(args.file) as logFile:
        log = (logFile.readlines())
        list = []
        for line in log:  
            match = re.findall('\.[a-z][a-z][a-z] ', line)
          
            if len(match) == 0:
                continue
            else:
         #       print(match)
                list.append(match)
        
       
  
    # intilize a null list 
        unique_list = [] 
      
    # traverse for all elements 
        for x in list: 
        # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
    
        i = 0
        for j in unique_list:
            if i < len(unique_list) - 1:
                broj=unique_list[i]
                br = list.count(unique_list[i])              
                print('{} - {}'.format(unique_list[i], br))
                i = i + 1
else:
    print ("File not exist")
