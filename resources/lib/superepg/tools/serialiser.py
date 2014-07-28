'''
Created on 29 Jun 2014

@author: Ian
'''

from resources.lib.t0mm0.common.addon import Addon

class Serialiser(object):
    '''
    classdocs
    '''
    ADDON_NAME = "script.service.superepg";
    
    @staticmethod
    def saveChannels(channels):
        try:
            addon = Addon(Serialiser.ADDON_NAME);
            addon.save_data("channel_data", channels);
        except:
            return;
        
    @staticmethod
    def loadChannels():
        addon = Addon(Serialiser.ADDON_NAME);
        return addon.load_data("channel_data");
    
    @staticmethod
    def setOpenGui(value):
        addon = Addon(Serialiser.ADDON_NAME);
        addon.save_data("openGui", value);
        
    @staticmethod
    def getOpenGui():
        addon = Addon(Serialiser.ADDON_NAME);
        return addon.load_data("openGui");
    
    @staticmethod
    def setOpenMain(value):
        addon = Addon(Serialiser.ADDON_NAME);
        addon.save_data("openMain", value);
        
    @staticmethod
    def getOpenMain():
        addon = Addon(Serialiser.ADDON_NAME);
        return addon.load_data("openMain");
    
    @staticmethod
    def setOpenManager(value):
        addon = Addon(Serialiser.ADDON_NAME);
        addon.save_data("openManager", value);
        
    @staticmethod
    def getOpenManager():
        addon = Addon(Serialiser.ADDON_NAME);
        return addon.load_data("openManager");
        