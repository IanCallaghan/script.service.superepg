'''
Created on 19 Jun 2014

@author: Ian
'''
from resources.lib.superepg.grabbers.episodeGrabber import EpisodeGrabber

class UnwatchedOnlyGrabber(EpisodeGrabber):
    '''
    classdocs
    '''
        
    def grabNextEpisode(self, episodes, number):
        i = 0;
        for episode in episodes:
            if episode["playcount"] == 0:
                if i == number:
                    return episode;
                i = i + 1;
                
    def getRefreshable(self):
        return True;
    
    def getName(self):
        return "Unwatched Only Grabber";