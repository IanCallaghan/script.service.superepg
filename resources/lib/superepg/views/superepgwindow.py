import xbmcgui;
import xbmcaddon;
import sys;
import time;
from resources.lib.xbmctools.xbmcactions import XbmcActions;
from resources.lib.superepg.views.listinggrid import ListingGrid

CONTROL_CURRENT_SHOW_DESC = 6003;
CONTROL_CURRENT_SHOW_TITLE = 6001;
CONTROL_CURRENT_SHOW_TIME = 6002;
CONTROL_TIME_NOW = 7000;

class Gui( xbmcgui.WindowXML ):

    channels = [];
    currentShowDescLbl = None;
    currentShowTitleLbl = None;
    currentShowTimeLbl = None;
    templateBtn = {};
    lastTime = 0;
    started = False;
    listingGrid = None;

    def __new__(cls):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        return super(Gui, cls).__new__(cls, 'script-tvguide-main.xml', ADDON.getAddonInfo('path'))

    def __init__(self):
        sys.stdout.write("Opening EPG \n")
        super(Gui, self).__init__()

    def onInit(self):
        if not self.started:
            self.currentShowDescLbl = self.getControl(CONTROL_CURRENT_SHOW_DESC);
            self.currentShowTitleLbl = self.getControl(CONTROL_CURRENT_SHOW_TITLE);
            self.currentShowTimeLbl = self.getControl(CONTROL_CURRENT_SHOW_TIME);
            self.started = True;
            self.listingGrid = ListingGrid(self, self.channels);


    def onAction(self, action):
        changedIndex = 0;
        channelChangedIndex = 0;

        if action.getId() == XbmcActions.ACTION_LEFT:
            changedIndex -= 1;
        elif action.getId() == XbmcActions.ACTION_RIGHT:
            changedIndex += 1;
        elif action.getId() == XbmcActions.ACTION_DOWN:
            channelChangedIndex += 1;
        elif action.getId() == XbmcActions.ACTION_UP:
            channelChangedIndex -= 1;
        elif action.getId() == XbmcActions.KEY_NAV_BACK:
            self.started = False;
            self.close()
        elif action.getId() == XbmcActions.ACTION_SELECT_ITEM:
            self.listingGrid.selectedListing.play();    

        self.listingGrid.selectChannelListing(channelChangedIndex, changedIndex);
        self.mainLoop(self.lastTime);
   
    def mainLoop(self, newTime):
        self.lastTime = newTime;  
        
        timeNow = time.time();
        if self.listingGrid != None:
            self.listingGrid.getListingsInView(self.lastTime); 
            self.currentShowDescLbl.setText(self.listingGrid.selectedListing.description);
            self.currentShowTitleLbl.setLabel(self.listingGrid.selectedListing.getTitle());
            self.currentShowTimeLbl.setLabel(self.listingGrid.selectedListing.getTimeDetails());
        timeDiff = time.time() - timeNow;
        sys.stdout.write("Update Listings Took: " + str(timeDiff) + "\n");         
        
        return;