'''
Created on 28 Jun 2014

@author: Ian
'''
from resources.lib.superepg.controllers.debugManager import DebugManager
import sys;
from resources.lib.superepg.tools.serialiser import Serialiser
from resources.lib.xbmctools.xbmcnotifications import Notifier
from resources.lib.superepg.tools import supercache
from resources.lib.superepg.controllers.channelManager import ChannelManager

class MainManager(object):
    '''
    classdocs
    '''
    debugManager = None;
    channelManager = None;
    
    @staticmethod
    def start():                           
        Notifier.notify("starting superepg", 1)
        MainManager.debugManager = DebugManager(True);
        sys.stdout.write("Starting SuperEpg Addon \n");
        
        #channelOb = supercache.LibraryCache.getChannels();
        
        MainManager.channelManager = ChannelManager();
        MainManager.channelManager.start(1, False);
        
        Serialiser.setOpenGui(False);
        
    @staticmethod
    def startGui():
        Serialiser.setOpenMain(True);