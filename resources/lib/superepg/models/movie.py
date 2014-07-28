'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.models.iDisplayShow import IDisplayShow;

class Movie(IDisplayShow):
    '''
    classdocs
    '''

    def __init__(self, movieData):
        self.json = movieData;
        
    def getDescription(self):
        return self.json["plot"];
    
    def getTitle(self):
        return self.json["title"];
    
    def getLength(self):
        return self.json["runtime"] / 60;
    
    def getFile(self, ):
        return self.json["file"];