
class author_date():
    def __init__(self, author, date):
        self.author = author
        self.date = date

    def update_author(self, author):
        self.author  = author

    def update_date(self, date):
        self.date = date

    def __str__(self):
        return '\t'.join([self.author, self.date])


def extract_file_author_date_from_first_git_commit_log(logfile):
    '''
    logfile: path of git log with --name-only option
        how to create: git log --name-only > logfile1
    
    Returns: 
        file_author_date: dictionary
            key: file name
            value: author_date instance
    '''

    file_author_date = {}
    
    in_log_record = False
    after_commit_message = False
    
    with open(logfile, 'r') as f:
        for line in f:
            if line.find('Author:') == 0:
                author = line.strip()[8:]
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
                    file = line.strip()
                    file_author_date[file]= author_date(author, date)

                if line.find('Date:')==0:
                    date = line.strip()[8:]
                if line.find('    ')==0: # to detect indent of commit message
                    after_commit_message=True

    return file_author_date

if __name__ == '__main__':
    
    logfile = 'git_log_with_filenames.txt'
    author_tobe_replaced = {'sub_string@tobe.replaced.jp':'Full String <after@replaced.jp>'}

    file2author_date = extract_file_author_date_from_first_git_commit_log(logfile)

    for file, a_d in file2author_date.items():
        for ar in author_tobe_replaced:
            if a_d.author.find(ar)>-1:
                a_d.update_author( author_tobe_replaced[ar] )
        print( '\t'.join([file, str(a_d)]))
