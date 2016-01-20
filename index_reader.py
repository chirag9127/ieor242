from file_reader import FileReader

YEAR = 2015
QUARTER = 'QTR1'

class IndexReader(object):
    def __init__(self, year=YEAR, quarter=QUARTER):
	self.year = year
	self.quarter = quarter
        self.fr = FileReader()
        # self.download_index_file()

    def download_index_file(self):
        index_name = 'edgar/full-index/{0}/{1}/company.idx'.format(self.year, self.quarter)
        local_file = 'files/index/'
        self.fr.download(index_name, local_file)

    def build_dictionary(self):
        f = open('files/index/company.idx', 'rb')
        line_num = 1
        for line in f:
            if line_num < 11:
                line_num += 1  
                continue
            line = line.split('   ')
            print line
            break 

ir = IndexReader()
ir.build_dictionary()
