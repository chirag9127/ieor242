'''
Input: Google 10-K 2014

Output: Dictionary containing financial metrics

Usage: Python financial_scraper.py 169 170 171 172 173 174 

Financial tables start from #169
TODO: Automate table selection
'''

import sys, re
from bs4 import BeautifulSoup

d = {}

file_to_parse = 'files/google/0001288776-15-000008.txt'

def parse_rows(rows):

    results = []
    #print("table has: ",len(rows)," rows")

    for row in rows:
        table_data = row.find_all('td')

        if table_data:
            results.append([data.get_text() for data in table_data]) 

    result_non_empty = []
 

    # Clear empty rows and remove undesirable values
    for i in results:
        for j in i:
            if len(j)>=1 and j not in ('\xa0','$',')'):
                result_non_empty.append(j) 

    # Fix the shitty closing braces for negative numbers

    result_non_empty = [re.sub(r'^\(\d{1,10}.*',j+')',j) for j in result_non_empty]

    #print(result_non_empty)

    return result_non_empty

def get_table(t):

        try:
            rows = t.find_all('tr')            
        except AttributeError as e:
            print('No rows found')
            return 1

        # Get data
        table_data = parse_rows(rows)

        return table_data

def generate_dict(td):

    new_list = []
    #print("length of old list is: ",len(td))

    # Concatenate text headers
    l = len(td)
    
    for i in range(0, l):
        try:
            if re.findall(r'[a-z|A-Z]',td[i]) and re.findall(r'[a-z|A-Z]',td[i+1]):
                new_list.append(td[i]+td[i+1])
                del(td[i+1])
                l = l-1
            else:
                new_list.append(td[i])
        except IndexError as e:
            break 
               

    #print("length of new list is: ",len(new_list))
    #print(new_list)        

    #Concatenate "year ending" 
    l = len(new_list)

    new_list1 = new_list

    year_headers = []

    for i in range(1,l):
        try:
            if int(new_list1[i]) in range(2000, 2020):
                new_list1[i] = new_list[0]+new_list1[i]
                year_headers.append(new_list1[i])
                #del(new_list1[i])
        except ValueError as e:
            break

    del(new_list1[0])

    #print(new_list1)
    #print("Headers are: ",year_headers)

    keys = []
    values = []

    for i in new_list1:
        if re.search(r'[a-z|A-Z]',i) and i not in year_headers:
            keys.append(i)
        elif i not in year_headers:
            values.append(i)
        else:
            continue

    # print("Keys are: ",keys)
    # print("Values are: ",values)


    i = 0
    j = len(year_headers)

    for key in keys:
        # if key in d.keys():
        #     try:
        #         key = str(str(key)+[1])
        #     except TypeError as t:
        #         print(key)
        d1 = {}
        for i in range(len(year_headers)):
            d1[year_headers[i]] = values[i]
        
        d[key] = d1
        del(values[0:j])
        #i = i+len(year_headers)
        #j = j-len(year_headers)

    
            



def main():


    with open(file_to_parse, 'r') as txt_file:
            txt = txt_file.read()


    soup = BeautifulSoup(txt,"html.parser")

    tables = []

    # Get table
    try:
        tables = soup.find_all('table')

        print("Found: ",len(tables)," tables")


    except AttributeError as e:
        print('No tables found')
        return 1

    for i in range(1,len(sys.argv)):

        table = tables[int(sys.argv[1])]

        print("Keeping table no: ",int(sys.argv[1]))

        table_data = get_table(table)
	print table_data

        dict_output = generate_dict(table_data)

    print("Output dictionary: ",d)


if __name__ == '__main__':
    status = main()
    sys.exit(status)
