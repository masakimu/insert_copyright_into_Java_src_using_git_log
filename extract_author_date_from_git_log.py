import sys

from file_author_date import FileAuthorDate

def extract_file_author_date_from_first_git_commit_log(logfile):
    '''
    logfile: path of git log with --name-only option
        how to create: git log --name-only > logfile1
    
    Yield: instance of file_author_date
    '''

    in_log_record = False
    after_commit_message = False
    
    with open(logfile, 'r') as f:
        for line in f:
            if line.find('Author:') == 0:
                end = len(line)
                pos_mail_addr= line.find('<')  # remove mail address from author name
                if pos_mail_addr > -1:
                    end = pos_mail_addr
                author = line.strip()[8:end]

                in_log_record = True
                continue

            if line.find('commit ')==0:
                in_log_record = False
                after_commit_message = False
                author = ''
                date = ''
                continue

            if in_log_record:
                if after_commit_message and len(line)>0 and line[0]!=' ' and line[0]!='\n': 
                    file_name = line.strip()
                    yield FileAuthorDate(file_name, author, date )

                if line.find('Date:')==0:
                    date = line.strip()[8:]
                if line.find('    ')==0: # to detect indent of commit message
                    after_commit_message=True


if __name__ == '__main__':
    argv=sys.argv
    argc=len(argv)

    if (argc!=2):
        print( 'Usage: python extract_author_date_from_git_log.py <Git Log File with File Names>')
        print( 'to generate git log: git log --name-only > logfile_name.txt')
        quit()
        
    logfile = argv[1]
    
    author_tobe_replaced = {'sub_string@tobe.replaced.jp':'Full String <after@replaced.jp>'}

    for f_a_d in extract_file_author_date_from_first_git_commit_log(logfile):
        for ar in author_tobe_replaced:
            if f_a_d.author.find(ar)>-1:
                f_a_d.update_author( author_tobe_replaced[ar] )
        print( str(f_a_d))

