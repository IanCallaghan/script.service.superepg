'''
Created on 21 Jun 2014

@author: Ian
'''

from resources.lib.superepg.listers.lister import Lister
from resources.lib.superepg.tools.array import Array
import random;

class RandomMovieLister(Lister):
    '''
    classdocs
    '''

    def __init__(self, amount):
        self.count = amount;
        return;
    
    def getName(self):
        return "Random Movie Lister"
        
    def createListings(self, tvShows, movies):
        if movies.__len__() == 0:
            return [];
        self.listings = Array();        
        i = 0;
                
        while i  < self.count:
            
            movie = random.choice(movies);
            self.addListing(movie);
            i = i + 1;
            
        self.listings = self.listings.list;
        
        return self.listings;