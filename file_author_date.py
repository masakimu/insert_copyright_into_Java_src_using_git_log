import dateutil.parser

class FileAuthorDate():
    def __init__(self, file, author, date):
        self.file =file
        self.author  = author
        # convert 'Wed May 30 20:29:47 2018 +0900' to '2018-05-30 20:29:47 +9000'
        self.datetime = str(dateutil.parser.parse(date))

    def update_author(self, author):
        self.author  = author

    def update_date(self, date):
        self.datetime = str(dateutil.parser.parse(date))

    @property
    def date(self):
        return str(self.datetime)
        
       
    def __str__(self):
        return '\t'.join([self.file, self.author, str(self.date)])
