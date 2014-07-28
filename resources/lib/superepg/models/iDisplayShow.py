'''
Created on 17 Jun 2014

@author: Ian
'''

class IDisplayShow(object):
    '''
    classdocs
    '''

    json = {};
    
    def __init__(self, params):
        '''
        Constructor
        '''
    def grabNext(self):
        return None;  
    
    def getDescription(self):
        return "description";
    
    def getTitle(self):
        return "title";
    
    def getLength(self):
        return 99;
    
    def getSeason(self):
        return -1;
    
    def getEpisode(self):
        return -1;
    
    def playContent(self, player):
        pass;