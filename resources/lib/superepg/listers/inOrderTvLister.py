'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.listers.lister import Lister
from resources.lib.superepg.tools.array import Array

class InOrderTvLister(Lister):
    '''
    classdocs
    '''


    def __init__(self, amount, epCount, movLister):
        self.episodesBeforeFilm = epCount;
        self.count = amount;
        self.movieLister = movLister;
        return;
    
    def getName(self):
        return "In Order Tv Lister"
        
    def createListings(self, tvShows, movies):
        self.listings = Array();
        
        i = 0;
        tvi = 0;
        moviei = 0;
        movieCount = 0;
        tvLength = tvShows.__len__();
        
        movieListings = self.movieLister.createListings(tvShows, movies);
        moviesLength = movieListings.__len__();
        
        if moviesLength == 0 and tvLength == 0:
            self.listings = [];
            return self.listings;
        
        while i  < self.count:
            
            if (moviei == self.episodesBeforeFilm and moviesLength > 0) or tvLength == 0:
                self.listings.push(movieListings[movieCount]);
                moviei = 0;
                movieCount = movieCount + 1;
            else:
                show = tvShows[tvi];
                self.addListing(show);
                
                tvi = tvi + 1;
                if tvi == tvLength:
                    tvi = 0;
                
                moviei = moviei + 1;
                
            i = i + 1;
            
        self.listings = self.listings.list;
        
        return self.listings;