# replace author and since in license header with those extracted from first commit log
# 
# example: before -> afeter
#   @author: Mass++ Users Group =>
#      @author Mass++ Users Group
#      @author Masaki Murase
#   @since: 2018 => @since: 2018-05-30 20:29:47 +9000
#           (date is used as version of each source code in Mass++ ver 4 or lator)

import os
import shutil
import csv

from file_author_date import FileAuthorDate

prefix_author = '@author'
prefix_since = '@since'

str_license_start = 'BSD 3-Clause License'
str_license_end = 'Copyright (c) 2018, Mass++ Users Group'

def reader_fileauthordate(csvreader):
    for row in csvreader:
        if len(row)==3:
            yield FileAuthorDate(*row)

def replace_line(line, target, insert):
    new_line = ''
    found = False
    newline = line
    
    pos = line.find(target)
    if pos>-1:
        found = True

        # keep original endline 
        endline = ''
        if line[-2] == '\r':
            endline = line[-2]
        endline=endline+line[-1]
        newline = line[0:pos] + target + ' ' + insert + endline
        
    return [found, newline]

def replace_license_header(f_output, f_input, fad):
    in_license_header = False
    finished_license_header = False
    
    found_first_author = False
    found_first_since = False
    is_file_replaced = False

    for line in f_input:
            
        if in_license_header:
            is_replaced=False
            if not(found_first_author):
                found_first_author, newline = replace_line(
                    line, prefix_author, fad.author )
                is_replaced  = found_first_author
                is_file_replaced = is_replaced
                if is_replaced:
                    line=line.replace(':','')
                    line=line.replace('User','Users')
                    f_output.write(line) # leave user group as author
                    f_output.write(newline) # add first commiter as co-author
            if not(found_first_since) and not(is_replaced):
                found_first_since, newline = replace_line(
                    line, prefix_since, fad.date )
                is_replaced  = found_first_since
                is_file_replaced = is_replaced
                if is_replaced:
                    f_output.write(newline)
            if line.find(str_license_end)>-1:
                in_license_header = False
                finished_license_header = True
            if not(is_replaced):
                f_output.write(line)
        else:
            if not(finished_license_header):
                if line.find(str_license_start)>-1:
                    in_license_header=True
            f_output.write(line)

    return is_file_replaced
        
def update_file_header(fad):
    '''
    fad: instance of FileAuthorDate
    '''
    src_file = fad.file
    orig_file= src_file+'.orig'
    temp_file= src_file+'_tmp'

    is_replaced=False
    
    if os.path.isfile(src_file):
        with open(temp_file,'w') as f_temp:
            with open(src_file, 'r') as f_orig:
                is_replaced = replace_license_header(f_temp, f_orig, fad)

        if is_replaced:
            try:
                os.rename(src_file, orig_file)
            except:
                print('source file({0}) was not copied to orig file({1})'.format(src_file, orig_file))
            else:
                os.rename(temp_file, src_file)
                print('succeeded replacement for: {0}'.format(src_file))
        else:
            os.remove(temp_file)
            print('not replacement for :{0}'.format(src_file))
    else:
        print('not existed: {0}'.format(src_file))
#list_fad = 'test_list_fad.txt'
list_fad = 'list_author4.txt' # no email address

with open(list_fad,'r') as f:
    csvreader = csv.reader(f, delimiter='\t')
    for fad in reader_fileauthordate(csvreader):
        update_file_header(fad)
        
        
        



