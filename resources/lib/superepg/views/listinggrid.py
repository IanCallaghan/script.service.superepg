'''
Created on 11 Jul 2014

@author: Ian
'''
import xbmcgui;
import sys;
from resources.lib.superepg.models.channel import Channel
from resources.lib.superepg.tools.array import Array
from resources.lib.superepg.views.buttoncache import ButtonCache
from resources.lib.superepg.tools.superchannel import EpgButton

EPG_Y = 75;
EPG_X = 9;
EPG_CHANNEL_WIDTH = 150;
EPG_CHANNEL_HEIGHT = 60;
EPG_CHANNEL_EPISODE_GAP = 2;
EPG_CHANNEL_GAP = 4;
EPG_EPISODE_GAP = 4;
EPG_EPISODE_MULT = 10;
EPG_MAX_WIDTH = 1280;
EPG_MAX_HEIGHT = 450;
EPG_TIMEBAR_MINS = 10;
EPG_TIMEBAR_HEIGHT = 455;

class ListingGrid(object):
    '''
    classdocs
    '''
    window = xbmcgui.Window;
    
    xOffset = 0;
    yOffset = 0;
    channels = [];
    buttonCache = None;
    timeBarImg = None;
    
    selectedIndex = 0;
    selectedChannelIndex = 0;
    selectedListing = None;
    lastTime = 0;
    
    minX = EPG_X + EPG_EPISODE_GAP + EPG_CHANNEL_EPISODE_GAP + EPG_CHANNEL_WIDTH;
    maxX = EPG_MAX_WIDTH;
    minY = EPG_Y;
    maxY = EPG_MAX_HEIGHT;

    def __init__(self, window, channels):
        '''
        Constructor
        '''
        self.window = window;
        self.channels = channels;
        self.buttonCache = ButtonCache(window);
        
        self.selectedListing = self.channels[0].lister.listings[0];
        
        toAdd = Array();
        for channel in self.channels:
            toAdd.push(self.createChannel(channel));
        self.window.addControls(toAdd.list);
        self.addTimeBar();
        
        return;
    
    def addTimeBar(self):
        self.timeBarImg = EpgButton.getTimeBarImg(0, EPG_Y, 2, EPG_TIMEBAR_HEIGHT - EPG_Y);
        self.window.addControl(self.timeBarImg);
        return;
    
    def createChannel(self, channel):
        ch = channel;
        x = EPG_X; height = EPG_CHANNEL_HEIGHT
        ch.button = EpgButton.getChannelBtn(EPG_X, 0, EPG_CHANNEL_WIDTH, height, ch.name, True);
        ch.button.setVisible(False);
        x = x + ch.button.getWidth() + EPG_CHANNEL_EPISODE_GAP;
        return ch.button;
        
    def getListingsInView(self, time):
        self.lastTime = time;
        channel = Channel();
        listingsInView = Array();
        y = EPG_Y;
        i = 0;
        sys.stdout.write("LISTING GRID UPDATE \n");
        self.buttonCache.clear();
        button = self.buttonCache.getNextButton();
        
        for channel in self.channels:
            x = EPG_X;
            started = False;
            finished = False;
            if y + self.yOffset > EPG_MAX_HEIGHT:
                channel.setVisible(False);
            elif y + self.yOffset < EPG_Y:
                channel.setVisible(False);
            else:
                channel.setVisible(True); 
                
            channel.button.setPosition(x,y + self.yOffset);
            
            if channel.visible:
                #sys.stdout.write("Updating Channel " + channel.name + "\n");
                xPlus = EPG_X + EPG_EPISODE_GAP + EPG_CHANNEL_EPISODE_GAP + EPG_CHANNEL_WIDTH + self.xOffset;  
                for listing in channel.lister.listings:
                    yPos = y + self.yOffset;
                    xPos = int((listing.getPlayTime(time) / 60) * -1 * EPG_EPISODE_MULT) + (EPG_TIMEBAR_MINS*EPG_EPISODE_MULT);
                    xPos += xPlus;
                    if self.crop(xPos, yPos, listing, button):
                        button = self.buttonCache.getNextButton();
                        listingsInView.push(listing);
                    xPlus += EPG_EPISODE_GAP;
                                
                    width = listing.length * EPG_EPISODE_MULT; 
                    if xPos + width >= self.minX:
                        started = True;
                    if xPos > self.maxX:
                        finished = True;
                        
                    if started and finished:
                        listing.view.visible = False;
                        break;
                        
            y += EPG_CHANNEL_HEIGHT + EPG_EPISODE_GAP;
            i += 1;
            
        self.buttonCache.postCleanup();
        self.focusListing();
        return;
    
    def crop(self, x, y, listing, button):
        width = listing.length * EPG_EPISODE_MULT;        
        retVal = True;
        listing.view.visible = False;
        
        button.setPosition(x, y);
        
        if x + width <= self.minX:
            return False;
        elif x <= self.minX:
            width = width - (self.minX - x);
            #x = minX;
            button.setPosition(self.minX, y);
        elif x + width > self.maxX:
            width = self.maxX - x;
            
        if x >= self.maxX:
            return False;
        if y < self.minY:
            return False;
        if y > self.maxY:
            return False;
            
        if retVal:
            button.setWidth(width);
            button.setHeight(EPG_CHANNEL_HEIGHT);
            button.setLabel(listing.title);
            listing.view.setPos(x,y);
            listing.view.button = button;
            listing.view.visible = True;
            #sys.stdout.write(button.getLabel() + "\n");
            button.setVisible(True);

        return retVal;
    
    def getClosestListing(self, channel, channelIndex):
        listingX = self.selectedListing.view.button.getX();
        listingMaxX = listingX + self.selectedListing.view.button.getWidth();
        i = 0;
        newIndex = -1;
        for listing in channel.lister.listings:
            if listing.view.button != None:
                newListX = listing.view.button.getX();
                newListMaxX = newListX + listing.view.button.getWidth();
                if newListMaxX < 0 or not listing.view.visible:
                    i += 1;
                    continue;
                if newListX >= listingX and newListX <= listingMaxX and channelIndex == 1:
                    newIndex = i;
                if newListX <= listingX and newListMaxX >= listingX and channelIndex == -1:
                    newIndex = i;
                if newListX <= listingX and newListMaxX >= listingMaxX:
                    return i;
                if newListX >= listingX and newListMaxX <= listingMaxX:
                    return i;
            i += 1;
        if newIndex == -1:
            return i;
        return newIndex;
    

    def selectChannelListing(self, channelIndex, index):
        newIndex = self.selectedIndex + index;
        
        newChannelIndex = self.selectedChannelIndex;
        channel = None;
        while (channel == None or not channel.enabled) and channelIndex != 0:
            newChannelIndex = newChannelIndex + channelIndex;
            channel = self.channels[newChannelIndex];
        channel = self.channels[newChannelIndex];
        
        if newChannelIndex < 0:
            return;
        
        if not channel.visible:
            self.yOffset += (channelIndex * EPG_CHANNEL_HEIGHT * -1) + (EPG_EPISODE_GAP * channelIndex * -1);
            self.getListingsInView(self.lastTime);#mainLoop(self.lastTime);
        
        if channelIndex != 0:
            newIndex = self.getClosestListing(channel, channelIndex);                    
        
        listingLen = channel.lister.listings.__len__();
        newListing = None;
        if newIndex < 0:
            return;
        if newIndex < listingLen:
            newListing = channel.lister.listings[newIndex];
            
        
        if channelIndex != 0 or (newListing != None and newListing.view.visible):
            self.selectedListing = newListing;
            #self.window.setFocus(self.selectedListing.view.button);
            self.selectedIndex = newIndex;
            self.selectedChannelIndex = newChannelIndex;
        elif newIndex < listingLen:
            self.xOffset += index * -60 * EPG_EPISODE_MULT;
            if self.xOffset < 0:
                return;
            
        if self.xOffset > 0:
                self.xOffset = 0;
            
    def focusListing(self):
        if self.selectedListing != None and self.selectedListing.view.button != None:
            if not self.selectedListing.view.visible:
                self.selectChannelListing(0, 1);
            self.window.setFocus(self.selectedListing.view.button);
        return;
                
            
        
        