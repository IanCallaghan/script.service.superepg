'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.listers.lister import Lister
from resources.lib.superepg.tools.array import Array

class InOrderMovieLister(Lister):
    '''
    classdocs
    '''

    def __init__(self, amount):
        self.count = amount;
        return;
    
    def getName(self):
        return "In Order Movie Lister"
        
    def createListings(self, tvShows, movies):
        self.listings = Array();
        
        i = 0;
        moviei = 0;
        movieLength = movies.__len__();
        
        while i  < self.count:
            
            movie = movies[moviei];
            self.addListing(movie);
                
            moviei = moviei + 1;
            if moviei == movieLength:
                moviei = 0;
                
            i = i + 1;
            
        self.listings = self.listings.list;
        
        return self.listings;