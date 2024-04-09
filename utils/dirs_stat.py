'''
Find the number of files and the total number of lines in a specific directory list
'''

import os
import fileinput
import datetime
from pprint import pprint as pp

dir_list = [
    "/home/jack/Algorithm/",
    "/home/jack/DataStructure/"
]

def count(dirs):
    '''save as dirlist = [
        {
            'dir' => dirname
        },
        {
            'total_files' => filecount
        },
        {
            'total_lines' => total_lines
        }
    ]'''
    dirs_stat = []

    # iter dirs
    for dir in dirs:
        # each dir stat
        total_lines = 0
        total_files = 0
        dir_stat = {}

        for dirpath, _dirnames, filenames in os.walk(dir):
            #get filepath for exception
            for file in filenames:
                filepath = os.path.join(dirpath, file)
                
                try:
                    # open fiel and count lines
                    with open(filepath, mode='r', encoding='utf-8') as fp:
                        # get total lines
                        lines = sum(1 for line in fp)
                        total_lines += lines
                        total_files += 1
                
                except UnicodeEncodeError:
                    print('skipping file => {} due to unicodeDecodeError'.format(filepath))
                    # continue to next file
                    continue
                
                except Exception as e:
                    print('error processing file {}, error => {}'.format(filepath, e))
                    continue
        
        dir_stat['dir'] = dir
        dir_stat['total_files'] = total_files
        dir_stat['total_lines'] = total_lines
        dirs_stat.append(dir_stat)
    return dirs_stat           

dirs_stat = count(dir_list)

for dir_stat in dirs_stat:
    pp(dir_stat)
