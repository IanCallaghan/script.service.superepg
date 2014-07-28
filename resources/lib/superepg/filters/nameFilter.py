'''
Created on 21 Jun 2014

@author: Ian
'''
from resources.lib.superepg.filters.filter import Filter;

class NameFilter(Filter):

    def apply(self, objects):
        filteredShows = [];
        i = 0;
        for show in objects:
            for name in self.params:
                if name == show.json["title"]:
                    filteredShows.insert(i, show);
                    i = i + 1;
        return filteredShows;
    
    def getName(self):
        return "Name Filter"