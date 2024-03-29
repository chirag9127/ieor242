import bs4, re

DEFAULT_FILENAME = 'files/google/0001288776-15-000008.txt'


class ParseFiling(object):
    def __init__(self, filename=DEFAULT_FILENAME):
        self.file_to_parse = filename
        with open(self.file_to_parse, 'r') as txt_file:
            self.txt = txt_file.read()

    def find_div_with_text(self):
        soup = bs4.BeautifulSoup(self.txt)
        scores = soup.find_all(text=re.compile('DISCUSSION AND ANALYSIS'))
        divs = [score.parent.parent.parent.parent.parent.parent.parent.parent for score in scores]
        all_text = divs[0].getText()
	all_text = all_text[:all_text.find('FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA')]
	print all_text
        return all_text


pf = ParseFiling()
pf.find_div_with_text()
