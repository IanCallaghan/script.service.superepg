'''
Created on 20 Jun 2014

@author: Ian
'''
import time;
from resources.lib.superepg.listers.inOrderTvLister import InOrderTvLister
from resources.lib.superepg.filters.genreFilter import GenreFilter
from resources.lib.superepg.filters.filterTypes import FilterTypes
from resources.lib.superepg.grabbers.unwatchedOnlygrabber import UnwatchedOnlyGrabber
from resources.lib.superepg.models.channel import Channel
from resources.lib.superepg.grabbers.randomGrabber import RandomGrabber
from resources.lib.superepg.listers.randomMovieLister import RandomMovieLister
from resources.lib.superepg.views.superepgwindow import Gui
from threading import Thread
from resources.lib.superepg.tools.serialiser import Serialiser
from resources.lib.superepg.tools.array import Array
from resources.lib.superepg.livetv.livetvgenerator import LiveTvGenerator
import sys;
from resources.lib.superepg.views.mainmenu import MainMenu
from resources.lib.superepg.views.channelmenu import ChannelMenu
from resources.lib.xbmctools.xbmcnotifications import Notifier

class ChannelManager(object):
    '''
    classdocs
    '''

    channels = [];
    timeNow = 0;
    updateInterval = 0;
    debugTimeAdvance = -1;
    gui = None;
    savePending = False;
    
    def __init__(self):
        return;                
        
    def start(self, updateInterval = 1, debug = False, debugTimeAdvance = -1):
        self.updateInterval = updateInterval;
        self.debugTimeAdvance = debugTimeAdvance;
        self.timeNow = time.time();
        
        if debug:
            self.debugChannels();        
        else:
            self.channels = Serialiser.loadChannels();
            
        if self.channels == None or self.channels == False:
            self.channels = [];
            
        self.startTimerThread();
        return;
    
    def startTimerThread(self):
        thread = Thread(target = self.startTimer);
        thread.start();
        
    def save(self):
        self.savePending = True;
        return;
        
    def startTimer(self):
        while True:
            if self.debugTimeAdvance != -1:
                self.timeNow += self.debugTimeAdvance;
            else:
                self.timeNow = time.time();#+= 60 * 3;
            self.update();
            
            if self.savePending:
                Serialiser.saveChannels(self.channels);
                self.savePending = False;
            
            if Serialiser.getOpenGui() == True:
                self.openGuiThread();
                Serialiser.setOpenGui(False);
                
            if Serialiser.getOpenMain() == True:
                self.openMainMenuThread();
                Serialiser.setOpenMain(False);
                
            if Serialiser.getOpenManager() == True:
                self.openMainManagerThread();
                Serialiser.setOpenManager(False);
                
            try:
                if self.gui != None and self.gui.started:
                    self.gui.mainLoop(self.timeNow);
            except:
                sys.stdout.write("unexpected error in epg view!");
            time.sleep(self.updateInterval);
    
    def openGuiThread(self):
        thread = Thread(target = self.openGui);
        thread.start();
        return;
    
    def openGui(self):
        self.gui = Gui()
        self.gui.channels = self.channels;#chanManager.channels;
        self.gui.doModal();
        self.gui.mainLoop(self.timeNow);
        
    def openMainMenuThread(self):
        thread = Thread(target = self.openMainMenu);
        thread.start();
        return;
    
    def openMainMenu(self):
        mainMenu = MainMenu();
        mainMenu.doModal();
        return;
    
    def openMainManagerThread(self):
        thread = Thread(target = self.openManagerMenu);
        thread.start();
        return;
    
    def openManagerMenu(self):
        channelMenu = ChannelMenu();
        channelMenu.channelManager = self;
        channelMenu.doModal();
        return;
    
    def update(self):
        for channel in self.channels:
            channel.updateTime(self.timeNow);
            
    def debugChannels(self):
        channels = Array();       
        
        for liveTvChannel in LiveTvGenerator.getLiveChannels():
            channels.push(liveTvChannel);
        
        #channels.push(self.createGenreChannel(0, "Comedy Action", ["Comedy", "Action"]));
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));    
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        
        channels.push(self.createGenreChannel(31, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(32, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(33, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(34, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(35, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(36, "Horror", ["Horror"]));
        channels.push(self.createGenreChannel(37, "Kids Action", ["Children", "Action"]));    
        channels.push(self.createGenreChannel(38, "Kids Comedy", ["Children", "Comedy"]));   
        channels.push(self.createGenreChannel(39, "Horror", ["Horror"]));         
        channels.push(self.createGenreChannel(40, "Kids Action", ["Children", "Action"]));  
        #channels.push(liveChannel);
    
        #channels.push(self.createGenreChannel(4, "Animation", ["Animation", "Comedy"]));  
        #channels.push(self.createGenreChannel(5, "Family", ["Family"]));   
          
        self.channels = channels.list;
                
    def createGenreChannel(self, num, name, genres):
        channela = Channel()
        channela.id = num;
        channela.name = name;
        
        channela.grabbers = [UnwatchedOnlyGrabber(), RandomGrabber()];
        channela.lister = InOrderTvLister(50, 5, RandomMovieLister(50));
        
        filterType = FilterTypes.NO_CONNECTOR;
        filters = Array();
        lastFilter = False;
        count = genres.__len__();
        i = 0;
        for genre in genres:
            i = i + 1;
            if i == count:
                lastFilter = True;
            filters.push(GenreFilter([genre], FilterTypes.TV_FILTER, filterType, lastFilter));
            filters.push(GenreFilter(genre, FilterTypes.MOVIE_FILTER));
            filterType = FilterTypes.AND_CONNECTOR;
        
        channela.filters = filters.list;
        channela.create(self.timeNow);
        channela.refreshGrabbers();
        return channela;
        