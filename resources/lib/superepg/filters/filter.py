'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.filters.filterTypes import FilterTypes

class Filter(object):
    '''
    classdocs
    '''
    label = "";
    objects = [];
    type = "";
    connectorType = FilterTypes.NO_CONNECTOR;
    isLast = True;
    params = [];
    
    def __init__(self, params, filterType, 
                 connectorType = FilterTypes.NO_CONNECTOR, isLast = True):
        self.type = filterType;
        self.params = params;
        self.connectorType = connectorType;
        self.isLast = isLast;

    def getType(self):
        return type;
    
    def apply(self, objects):
        return objects;
    
    def getName(self):
        return "No name set"
    
    def getOptions(self, filterType):
        return [];