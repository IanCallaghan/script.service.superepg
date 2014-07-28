'''
Created on 15 Jul 2014

@author: Ian
'''

import xbmcgui;
import xbmcaddon;
from resources.lib.xbmctools.xbmcactions import XbmcActions
from resources.lib.superepg.tools.serialiser import Serialiser

class MainMenu(xbmcgui.WindowXML):
    '''
    classdocs
    '''

    nowPlayingBtn = 2000;
    tvGuideBtn = 2001;
    channelManBtn = 2002;
    exitBtn = 2003;
    
    nowPlayingBtnSel = 3000;
    tvGuideBtnSel = 3001;
    channelManBtnSel = 3002;
    exitBtnSel = 3003;
    
    selectedIdx = 0;
    controls = [];
    selectedControls = [];
    
    started = False;

    def __new__(cls):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        return super(MainMenu, cls).__new__(cls, 'script-tvguide-channels.xml', ADDON.getAddonInfo('path'));

    def __init__(self):
        super(MainMenu, self).__init__();
        
    def onInit(self):      
        self.start();
        return;
    
    def start(self):
        if self.started:
            return;
        
        self.controls = [];
        self.selectedControls = [];
        
        self.nowPlayingBtn = self.getControl(self.nowPlayingBtn);
        self.tvGuideBtn = self.getControl(self.tvGuideBtn);
        self.channelManBtn = self.getControl(self.channelManBtn);
        self.exitBtn = self.getControl(self.exitBtn);
        
        self.nowPlayingBtnSel = self.getControl(self.nowPlayingBtnSel);
        self.tvGuideBtnSel = self.getControl(self.tvGuideBtnSel);
        self.channelManBtnSel = self.getControl(self.channelManBtnSel);
        self.exitBtnSel = self.getControl(self.exitBtnSel);
        
        self.controls.insert(0, self.nowPlayingBtn);
        self.controls.insert(1, self.tvGuideBtn);
        self.controls.insert(2, self.channelManBtn);
        self.controls.insert(3, self.exitBtn);
        
        self.selectedControls.insert(0, self.nowPlayingBtnSel);
        self.selectedControls.insert(1, self.tvGuideBtnSel);
        self.selectedControls.insert(2, self.channelManBtnSel);
        self.selectedControls.insert(3, self.exitBtnSel);
        
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
    
    def onFocus(self, controlId):
        self.setSelected(0);
        return
    
    def openTvGuide(self):
        Serialiser.setOpenGui(True);
        return;
    
    def openChannelManager(self):
        Serialiser.setOpenManager(True);
        return;
   
    def navigate(self):
        selectedBtn = self.controls[self.selectedIdx];
        
        if selectedBtn == self.tvGuideBtn:
            self.openTvGuide();
        elif selectedBtn == self.nowPlayingBtn:
            return;
        elif selectedBtn == self.channelManBtn:
            self.openChannelManager();
        elif selectedBtn == self.exitBtn:
            self.close();
        return;
    
    def setSelected(self, increase):
        self.selectedIdx += increase;
        length = self.controls.__len__();
        
        if self.selectedIdx < 0:
            self.selectedIdx = 0;
        if self.selectedIdx > length - 1:
            self.selectedIdx = length - 1;
            
        
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
        return;
        