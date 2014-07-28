'''
Created on 21 Jun 2014

@author: Ian
'''

from resources.lib.superepg.grabbers.episodeGrabber import EpisodeGrabber;
import random;

class RandomGrabber(EpisodeGrabber):
    '''
    classdocs
    '''
        
    def grabNextEpisode(self, episodes, number):
        episode = random.choice(episodes);
        return episode;
                
    def getRefreshable(self):
        return True;
    
    def getName(self):
        return "Random Grabber";