'''
Created on 29 Jun 2014

@author: Ian
'''
import xbmcgui

class PropertySetter(object):
    '''
    classdocs
    '''
    WINDOW_ID = 10000;
    TRUE = "true";
    FALSE = "false";
    
    PROP_OPEN_GUI = "PROP_OPEN_GUI";

    @staticmethod
    def setProperty(key, value):        
        win = xbmcgui.Window(PropertySetter.WINDOW_ID);
        win.setProperty(key, value);
        
    @staticmethod
    def getProperty(key):        
        win = xbmcgui.Window(PropertySetter.WINDOW_ID);
        win.getProperty(key)
        
    