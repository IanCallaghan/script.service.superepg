'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.models.iDisplayShow import IDisplayShow;
from resources.lib.superepg.tools.supercache import LibraryCache

class TvShow(IDisplayShow):
    '''
    classdocs
    '''

    episodes = [];
    filteredEpisodes = [];
    grabbers = [];
    selectedEpisode = None;
    grabberCounts = [];
    
    def __init__(self, showData):
        self.json = showData;
        
    def grabNext(self):
        i = 0;
        for grabber in self.grabbers:
            episode = grabber.grabNextEpisode(self.episodes, self.grabberCounts[i]);
            self.grabberCounts[i] = self.grabberCounts[i] + 1;
            i = i + 1;
            
            if episode != None:
                self.selectedEpisode = episode;
                return grabber;
            
        self.selectedEpisode = self.episodes[0];
        return None;
    
    def getDescription(self):
        return self.selectedEpisode["plot"];
    
    def getTitle(self):
        return self.json["title"];
    
    def getLength(self):
        return self.selectedEpisode["runtime"] / 60;
    
    def getFile(self,):
        return self.selectedEpisode["file"];
    
    def getSeason(self):
        return self.selectedEpisode["season"];
    
    def getEpisode(self):
        return self.selectedEpisode["episode"];
        
    def getEpisodes(self):
        self.episodes = LibraryCache.getEpisodes(self.json["tvshowid"]).episodes;
        self.filteredEpisodes = self.episodes;
    

    '''def getNextEpisodeUnwatched(self):
        if self.unwatchedCount <= 0:
            return None;
        return self.episodesUnwatched[0];

    def getNextShowLength(self):
        if self.unwatchedCount <= 0:
            return 30;
        return self.episodesUnwatched[0]["runtime"]/60;
    
    def getEpisodes(self):
        self.episodes = LibraryCache.getEpisodes(self.json["tvshowid"]).episodes;
        self.episodesUnwatched = [];

        i = 0;
        for episode in self.episodes:
            if episode["playcount"] <= 0:
                self.episodesUnwatched.insert(i, episode);
                i = i + 1;
        self.unwatchedCount = i;'''
        