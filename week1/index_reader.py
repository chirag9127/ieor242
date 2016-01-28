from file_reader import FileReader

YEAR = 2015
QUARTER = 'QTR1'

class IndexReader(object):
    def __init__(self, year=YEAR, quarter=QUARTER):
	self.year = year
	self.quarter = quarter
        self.fr = FileReader()
        # self.download_index_file()
        self.company_dictionary = self.build_dictionary()

    def download_index_file(self):
        index_name = 'edgar/full-index/{0}/{1}/company.idx'.format(self.year, self.quarter)
        local_file = 'files/index/'
        self.fr.download(index_name, local_file)

    def build_dictionary(self):
        company_dictionary = {}
        f = open('files/index/company.idx', 'rb')
        line_num = 1
        for line in f:
            if line_num < 11:
                line_num += 1  
                continue
            line = line.split('  ')
            count = 0
            values_extracted = {}
            for item in line:
                if item != '':
                    values_extracted[count] = item
                    count += 1
            company = values_extracted[0].strip()
            type = values_extracted[1].strip()
            cik = values_extracted[2].strip()
            date_filed = values_extracted[3].strip()
            file_name = values_extracted[4].strip()
            if type in ['10-Q', '8-K', '10-K']:
                if company not in company_dictionary:
                    company_dictionary[company] = [] 
                company_dictionary[company].append({'type': type, 'cik': cik, 'date_filed': date_filed, 'file_name': file_name})
        return company_dictionary

    def get_company(self, company_name):
        for key, value in self.company_dictionary.iteritems():
            if key.startswith(company_name):
                for file_dict in value:
                    print file_dict

