'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.models.listing import Listing

class Lister(object):
    '''
    classdocs
    '''
    
    listings = [];
    episodesBeforeFilm = 1;
    count = 0;
    movieLister = None;
    
    def __init__(self, time):
        self.time = time;
        '''
        Constructor
        '''
    def createListings(self, tvShows, movies):
        pass;
    
    def addListing(self, showOrMovie):
        listing = Listing();
        listing.displayShow = showOrMovie;
        #listing.button = EpgButton.getBtn(0, 0, showOrMovie.getLength(), 0, showOrMovie.getTitle());
        self.insertListing(listing)
        
    def insertListing(self, listing):
        self.listings.push(listing);
        
    def getName(self):
        return "Non name set"
        