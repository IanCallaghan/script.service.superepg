'''
Created on 17 Jun 2014

@author: Ian
'''
import sys;
from resources.lib.superepg.tools.array import Array;
from resources.lib.superepg.models.movie import Movie
from resources.lib.superepg.filters.filterTypes import FilterTypes
from resources.lib.superepg.models.tvShow import TvShow
from resources.lib.superepg.tools.supercache import LibraryCache

class Channel(object):
    '''
    classdocs
    '''
    
    LIBRARY = "Channel.Library";
    LIVE = "Channel.Live";

    name = "";
    id = 0;
    filters = [];
    tvshows = [];
    movies = [];
    selectedListing = 0;
    grabbers = [];
    lister = None;
    createdTime = 0;
    currentTime = 0;
    visible = True;
    type = LIBRARY;
    enabled = True;
    
    button = None;

    def __init__(self):
        pass;

    #Create channel
    def create(self, time):
        sys.stdout.write("Creating channel - name:" + self.name + " id:" + str(self.id) + "\n");
        self.createdTime = time;
        self.currentTime = time;
        self.getAllMovies();
        self.getAllTvShows();
        self.applyFilters();
        self.createListings();
        self.applyGrabbers();
        return;
    
    def getAllMovies(self):
        self.movies = Array();
        for json in LibraryCache.getMovies().movies:
            movie = Movie(json);
            self.movies.push(movie);
        self.movies = self.movies.list;
    
    def getAllTvShows(self):
        self.tvshows = Array();
        for json in LibraryCache.getTvShows().tvshows:
            tvShow = TvShow(json);
            self.tvshows.push(tvShow);
        self.tvshows = self.tvshows.list;
        

    def applyFilters(self):
        self.tvshows = self.applyFilterSet(FilterTypes.TV_FILTER, self.tvshows);
        self.movies = self.applyFilterSet(FilterTypes.MOVIE_FILTER, self.movies);
        '''for tvShow in self.tvshows:
            tvShow.getEpisodes();
            if sFilter.type == FilterTypes.EPISODE_FILTER:
                tvShow.filteredEpisodes = sFilter.apply(self.filteredEpisodes);'''
        return;
        
    def applyFilterSet(self, filterType, listOfObs):
        showLists = Array();
        showList = [];
        for sFilter in self.filters:
            if sFilter.type == filterType:
                if sFilter.connectorType == FilterTypes.NO_CONNECTOR or sFilter.connectorType == FilterTypes.OR_CONNECTOR:
                    showList = sFilter.apply(listOfObs);
                elif sFilter.connectorType == FilterTypes.AND_CONNECTOR:
                    showList = sFilter.apply(showList);
                    
                if sFilter.isLast:
                    showLists.push(showList);
                
        showLists = showLists.list;
        listOfObs = Array();
        for finalShowList in showLists:
            for show in finalShowList:
                listOfObs.push(show);
                
        return listOfObs.list;

    def getPreviousListing(self):
        return self.lister.listings[self.selectedListing-1];

    def createListings(self):
        self.lister.createListings(self.tvshows, self.movies);        
        
    def applyGrabbers(self):
        if self.type == self.LIVE:
            return;
        
        for tvshow in self.tvshows:
            tvshow.getEpisodes();
            tvshow.grabbers = Array();
            tvshow.grabberCounts = Array();
            for grabber in self.grabbers:
                tvshow.grabbers.push(grabber);
                tvshow.grabberCounts.push(0);
                
            tvshow.grabbers = tvshow.grabbers.list;
            tvshow.grabberCounts = tvshow.grabberCounts.list;
        
        time = self.createdTime;
        for listing in self.lister.listings:
            listing.grabDetails();
            listing.time = time;
            time += listing.length * 60;
        return;
    
    def refreshGrabbers(self):
        if self.type == self.LIVE:
            return;
        
        for tvshow in self.tvshows:
            tvshow.getEpisodes();
            tvshow.grabberCounts = Array();
            for grabber in tvshow.grabbers:
                tvshow.grabberCounts.push(0);
            tvshow.grabberCounts = tvshow.grabberCounts.list;
        
        for listing in self.lister.listings:
            if listing.enabled:
                listing.grabDetails();            
        return;
    
    def updateTime(self, time):
        self.currentTime = time;
        timeDiff = time - self.createdTime;
        
        if self.lister.listings.__len__() == 0:
            return;
        curListing = self.getNextActiveListing();
        refreshReq = False;
        
        '''sys.stdout.write("-------------------------\n")
        sys.stdout.write("Time Passed: " + str(timeDiff) + "\n")
        sys.stdout.write("Active Listing: " + curListing.title + "\n")
        sys.stdout.write("File: " + curListing.content + "\n")
        sys.stdout.write("Running for: " + str(curListing.getPlayTime(time)) + "\n")
        sys.stdout.write("Complete: " + str(curListing.getFinished(time)) + "\n")'''
        
        
        while curListing != None and curListing.getFinished(time):
            self.removeCurrentListing();
            curListing = self.getNextActiveListing();
            self.selectedListing = self.getListingIndex(curListing);
            refreshReq = True;
        
        if refreshReq:
            self.refreshGrabbers();
            
        if curListing == None:
            self.enabled = False;
            
        return;
    
    def getListingIndex(self, listing):
        i = 0;
        for listingLookup in self.lister.listings:
            if listing == listingLookup:
                return i;
            i += 1;
        return 0;
    
    def getNextActiveListing(self):
        for listing in self.lister.listings:
            if listing.enabled:
                return listing;
            
        return None;
    
    def removeCurrentListing(self):
        nextListing = self.getNextActiveListing();
        if nextListing != None:
            nextListing.enabled = False;
        self.lister.listings[0].view.remove();
        self.lister.listings.reverse();
        self.lister.listings.pop();
        self.lister.listings.reverse();
        
    def setVisible(self, value):
        #if self.visible != value:
        self.button.setVisible(value);
        self.visible = value;