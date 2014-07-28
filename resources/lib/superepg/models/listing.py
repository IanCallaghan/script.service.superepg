'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.tools.superplayer import SuperPlayer
from resources.lib.superepg.views.listingView import ListingView
import time;
class Listing:

    displayShow = None;
    view = ListingView();
    
    description = "";
    season = -1;
    episode = -1;
    title = "";
    length = 99;
    content = "";
    lastGrabberUsed = None;
    time = 0;
    player = SuperPlayer();
    enabled = True;
    
    def __init__(self):
        self.view = ListingView();
    
    def play(self):
        #player = SuperPlayer();
        SuperPlayer().play(self.content);
        
    def grabDetails(self):
        currentGrabber = self.displayShow.grabNext();
        
        if currentGrabber != self.lastGrabberUsed or self.lastGrabberUsed == None or self.lastGrabberUsed.getRefreshable():
            self.lastGrabberUsed = currentGrabber;
            self.getDetails();
        return;
    
    def getDetails(self):
        self.description = self.displayShow.getDescription();
        self.title = self.displayShow.getTitle();
        self.length = self.displayShow.getLength();
        self.content = self.displayShow.getFile();
        self.season = self.displayShow.getSeason();
        self.episode = self.displayShow.getEpisode();
        return;
    
    def getPlayTime(self, currentTime):
        return currentTime - self.time;
    
    def getFinished(self, currentTime):
        return (currentTime - self.time) > self.length * 60;
    
    def getTimeDetails(self):
        timeStart = time.localtime(self.time);
        timeEnd = time.localtime(self.time + self.length * 60);
        
        timeStartStr = self.getTimeFormat(timeStart.tm_hour) + ":" + self.getTimeFormat(timeStart.tm_min);
        timeEndStr = self.getTimeFormat(timeEnd.tm_hour) + ":" + self.getTimeFormat(timeEnd.tm_min);
        return timeStartStr + " - " + timeEndStr;
    
    def getTimeFormat(self, num):
        if num < 10:
            return "0" + str(num);
        return str(num);
    
    def getTitle(self):
        return self.title + " - Season:" + str(self.season) + " Episode:" + str(self.episode);
    
