import ftplib


GOOGLE_2015_Q1 = 'edgar/data/1288776/0001288776-15-000008.txt'
GOOGLE_LOCAL_FILE_DIRECTORY = 'files/google/'


class FileReader(object):
    
    def __init__(self):
        self.ftp_connection = ftplib.FTP('ftp.sec.gov', 
                                         'anonymous', 
                                         'chirag.mahapatra@berkeley.edu')

    def download(self, file_to_be_downloaded=GOOGLE_2015_Q1, local_file_path=GOOGLE_LOCAL_FILE_DIRECTORY):
        file_name = file_to_be_downloaded.split('/')[-1]
        local_file = open("{0}/{1}".format(local_file_path, file_name), "wb")
        self.ftp_connection.retrbinary('RETR %s' % file_to_be_downloaded, local_file.write)
        local_file.close()

    def __del__(self):
        self.ftp_connection.quit()

if __name__ == "__main__":
    fr = FileReader()
    fr.download()
