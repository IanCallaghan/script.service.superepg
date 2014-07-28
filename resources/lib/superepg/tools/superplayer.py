'''
Created on 15 Jun 2014

@author: Ian
'''

import xbmc
import sys;

class SuperPlayer(xbmc.Player):
    
    def __init__( self, *args ):
        pass

    def onPlayBackStarted(self):
        sys.stdout.write("playback started \n");

    def onPlayBackEnded(self):
        sys.stdout.write("playback ended \n");
                   
    def onPlayBackStopped(self):
        sys.stdout.write("playback stopped \n");
        
        