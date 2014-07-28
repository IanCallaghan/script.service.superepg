'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.filters.filter import Filter;
from resources.lib.xbmctools import xbmcvideolibrary
from resources.lib.superepg.filters.filterTypes import FilterTypes

class GenreFilter(Filter):


    def apply(self, objects):
        filteredShows = [];
        i = 0;
        for show in objects:
            for showGenre in show.json["genre"]:
                for genre in self.params:
                    if showGenre == genre:
                        filteredShows.insert(i, show);
                        i = i + 1;
        return filteredShows;
    
    def getName(self):
        return "Genre Filter"
    
    def getOptions(self, filterType):
        typeName = "";
        genres = [];
        if filterType == FilterTypes.MOVIE_FILTER:
            typeName = "movie";
            
        if filterType == FilterTypes.TV_FILTER:
            typeName = "tvshow";
            
        i = 0;
        for jsonOb in xbmcvideolibrary.VideoLibrary.GetGenres(typeName).genres:
            genres.insert(i, jsonOb["label"]);
            i += 1;
            
        return genres;