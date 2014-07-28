'''
Created on 15 Jul 2014

@author: Ian
'''

import xbmcgui;
import xbmcaddon;
from resources.lib.xbmctools.xbmcactions import XbmcActions
from resources.lib.superepg.views.spincontroloption import SpinControlOption
from resources.lib.superepg.livetv.livetvgenerator import LiveTvGenerator

class LiveChannleEditor(xbmcgui.WindowXML):
    '''
    classdocs
    '''
    inputForwardControls = [];
    liveChannels = [];
    nameControl = None;
    spinControl = None;
    submitBtn = None;
    cancelBtn = None;
    
    channelManager = None;
    channelMenu = None;
    
    def __new__(cls):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        return super(LiveChannleEditor, cls).__new__(cls, 'livechanneleditor.xml', ADDON.getAddonInfo('path'));

    def __init__(self):
        super(LiveChannleEditor, self).__init__();
        
        
    def onInit(self):      
        spincontrol = self.getControl(1000);
        
        self.nameControl = self.getControl(902);
        self.cancelBtn = self.getControl(9000);
        self.submitBtn = self.getControl(9001);
        
        self.liveChannels = LiveTvGenerator.getLiveChannels();
        
        channelNames = [];
        i = 0;        
        for liveTvChannel in self.liveChannels:
            channelNames.insert(i, liveTvChannel.name);
            i += 1;
        
        if channelNames.__len__() == 0:
            channelNames = ["No Channels"];
            
        self.inputForwardControls = [];
        self.spinControl = SpinControlOption(self, 1002, 1001, 1003, channelNames);
        self.inputForwardControls.insert(0, self.spinControl)
        
        self.setFocus(spincontrol)
        return;
    
    def onAction(self, action):
        focusedItem = self.getFocus();
        
        if action.getId() == XbmcActions.KEY_NAV_BACK:
            self.close();
        if action.getId() == XbmcActions.ACTION_SELECT_ITEM:
            if focusedItem == self.cancelBtn:
                self.close();
            if focusedItem == self.submitBtn:
                self.createChannel();
        
        for control in self.inputForwardControls:
            control.forwardInput(action.getId());
        return;
    
    def createChannel(self):
        selectedText = self.spinControl.getSelectedOption();
        channelName = self.nameControl.getText();
        
        selectedChannel = None;
        
        for channel in self.liveChannels:
            if channel.name == selectedText:
                selectedChannel = channel;
               
        selectedChannel.name = channelName;
        
        self.channelManager.channels.insert(self.channelManager.channels.__len__()-1, selectedChannel);
        
        self.channelMenu.start();
        
        self.close();
        
        return;
        