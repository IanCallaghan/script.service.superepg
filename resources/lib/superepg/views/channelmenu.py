'''
Created on 15 Jul 2014

@author: Ian
'''

import xbmcgui;
import xbmcaddon;
from resources.lib.xbmctools.xbmcactions import XbmcActions
from resources.lib.superepg.tools.serialiser import Serialiser
from resources.lib.superepg.views.livechanneleditor import LiveChannleEditor
from resources.lib.superepg.views.librarychanneleditor import LibraryChannelEditor

class ChannelMenu(xbmcgui.WindowXML):
    '''
    classdocs
    '''

    controlStart = 2000;    
    controlSelStart = 3000;
    controlAmount = 8;
    
    selectedIdx = 0;
    labelIdx = 0;
    controls = [];
    selectedControls = [];
    labels = [];
    
    started = False;
    channelManager = None;

    def __new__(cls):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        return super(ChannelMenu, cls).__new__(cls, 'channelmenu.xml', ADDON.getAddonInfo('path'));

    def __init__(self):
        super(ChannelMenu, self).__init__();
        
    def onInit(self):      
        self.start();
        return;
    
    def start(self):
        
        self.controls = [];
        self.selectedControls = [];
        self.labels = [];
        self.selectedIdx = 0;
        
        i = 0;
        
        while i < self.controlAmount:
            self.controls.insert(i, self.getControl(self.controlStart + i));
            self.selectedControls.insert(i, self.getControl(self.controlSelStart + i));
            i += 1;
            
        self.labels.insert(0, "New Library Channel");
        self.labels.insert(1, "New Live Channel");
        
        i = 2;
        
        for channel in self.channelManager.channels:
            self.labels.insert(i, channel.name);
            i += 1;
        
        self.setSelected(0);        
        self.started = True;
    
    def onAction(self, action):
        changedIndex = 0;

        if action.getId() == XbmcActions.ACTION_DOWN:
            changedIndex += 1;
        elif action.getId() == XbmcActions.ACTION_UP:
            changedIndex -= 1;
        elif action.getId() == XbmcActions.ACTION_SELECT_ITEM:
            self.navigate();
        elif action.getId() == XbmcActions.KEY_NAV_BACK:
            self.close()  

        self.setSelected(changedIndex);
        return;
    
    def navigate(self):
        selectedBtn = self.controls[self.selectedIdx];
        index = self.labelIdx + self.selectedIdx;
        channelIdx = index - 2;
        
        if index == 0:
            menu = LibraryChannelEditor();
            menu.channelManager = self.channelManager;
            menu.channelMenu = self;
            menu.doModal();
        elif index == 1:
            menu = LiveChannleEditor();
            menu.channelManager = self.channelManager;
            menu.channelMenu = self;
            menu.doModal();
        else:
            return;
        
        return;
    
    def updateLabels(self):
        i = self.labelIdx;
        for label in self.controls:
            if i < self.labels.__len__():
                label.setLabel(self.labels[i]);
            i += 1;
            
        i = self.labelIdx;
        for label in self.selectedControls:
            if i < self.labels.__len__():
                label.setLabel(self.labels[i]);
            i += 1;
            
    
    def setSelected(self, increase):
        self.selectedIdx += increase;
        length = self.controls.__len__();
        labelLen = self.labels.__len__();
        
        if self.selectedIdx < 0:
            self.selectedIdx = 0;
            self.labelIdx -= 1;
            if self.labelIdx < 0:
                self.labelIdx = 0;
                
        if self.selectedIdx > length - 1:
            self.selectedIdx = length - 1;
            self.labelIdx += 1;
            if self.labelIdx > labelLen - self.controlAmount:
                self.labelIdx = labelLen - self.controlAmount;   
                             
        if self.selectedIdx > labelLen - 1:
            self.selectedIdx = labelLen - 1;
            '''self.labelIdx += 1;
            if self.labelIdx > labelLen - self.controlAmount:
                self.labelIdx = labelLen - self.controlAmount;'''
            
        
        i = 0;        
        for label in self.controls:
            if i != self.selectedIdx:
                label.setVisible(True);
            else:
                label.setVisible(False);
            i += 1;
            
        i = 0;        
        for label in self.selectedControls:
            if i != self.selectedIdx:
                label.setVisible(False);
            else:
                label.setVisible(True);
            i += 1;
            
        self.updateLabels();
        return;
        