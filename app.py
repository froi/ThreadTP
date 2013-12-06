#! venv/bin/python

import ftplib
from glob import glob
import yaml
import logging
from multiprocessing import Pool

logging.basicConfig( filename='threadTP.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %message)s' )

class Config():
    """
    ThreadTP cofig class.
    Defaults:
        host: localhost
        port: 21
        user:
        password:
        docs_repo: ~/Documents/docs
        num_threads: 2
        file_types: ['.txt']
    """
    host = 'localhost'
    port = 21
    user = ''
    password = ''
    docs_repo = '~/Documents/docs'
    num_threads = 2
    file_types = ['.txt']

    def loadConfig(self, config_file="CONFIG.yml") :
        """ 
        Loads supplied configuration file. 
        If no path is passed then it will default to look for file in executing folder. 
        If file not found then class defaults will be used.
        """
        print 'loading config'
        try:

            with open(config_file, 'r') as f:
                if f is not None:
                    print 'found file: ', f
                    # TODO: set values only if there is values in the config file...

                    tmpConfig = yaml.load(f)

                    # FTP config
                    self.host = tmpConfig['server']['host']
                    self.port = tmpConfig['server']['port']
                    self.user = tmpConfig['credentials']['user']
                    self.password = tmpConfig['credentials']['password']
                    self.docs_repo = tmpConfig['config']['docs_repo']
                    self.num_threads = tmpConfig['config']['num_threads']
                    self.file_types = tmpConfig['config']['file_types']
        except IOError as e:
            print 'Config file not found or unable to open.'

def run():
    print 'entered run'
    pool = Pool(processes=config.num_threads, initializer=threadTP_init)
    
    for path, error in pool.imap_unordered(uploadFiles, createDocList(config.docs_repo, config.file_types)):
        if error:
            print "File %s upload failed. Error: " % path, error
    print "finished"

def threadTP_init():
    global ftpSession
    try:
        ftpSession = ftplib.FTP(config.host,config.user,config.password)
    except:
        print 'FTP session creation failed.'


def createDocList(docRepo, fileTypes):

    print 'entered createDocList'
    tmpDocsList = []
    for fileType in fileTypes:
        tmpDocsList += glob('%s*%s' % (docRepo, fileType) )

    return tmpDocsList

def uploadFiles(path):
    print 'entered uploadFiles', path

    with open(path, 'r') as tmpFile:
        try:
            ftpSession.storbinary('STOR %s' % tmpFile.name.split('/')[-1], tmpFile)
        except Exception as error:
            return path, error
        else:
            return path, None

if __name__ == '__main__':
    # TODO: added arg parsing for cli parameters

    config = Config()
    config.loadConfig()

    print 'Host: %s' % config.host
    print 'User: %s' % config.user
    print 'Password: %s' % config.password
    print 'File types: ', config.file_types
    print 'Number of threads: %d' % config.num_threads
    
    run()