'''
Created on 17 Jun 2014

@author: Ian
'''
from resources.lib.superepg.listers.lister import Lister
from resources.lib.superepg.tools.array import Array
import os;
import xbmc;
import sys;
from resources.lib.superepg.models.listing import Listing;
from resources.lib.superepg.livetv.livetvdbs import LiveTvDbs;

class LiveTvLister(Lister):
    '''
    classdocs
    '''
    channelNum = 0;
    name = "live";

    def __init__(self, channelNum):
        self.channelNum = channelNum;
        return;
        
    def createListings(self, tvShows, movies):
        self.listings = Array();
                    
        profilePath = xbmc.translatePath(os.path.join('special://userdata/Database', ''));
        if os.path.exists(profilePath):            
            cursor = LiveTvDbs.getDatabase(LiveTvDbs.EPGDB);
            cursor.execute("SELECT * FROM epg");
            data = cursor.fetchall();
            
            epgChannelNumber = data[self.channelNum][0];
            self.name = data[self.channelNum][1];
            executeStr = (str(epgChannelNumber),)
            
            cursor.execute("SELECT * FROM epgtags WHERE idEpg=? ORDER BY iStartTime", executeStr);
            epgListings = cursor.fetchall();
            
            executeStr = (self.name,);
            cursor = LiveTvDbs.getDatabase(LiveTvDbs.TVDB);
            cursor.execute("SELECT * FROM channels WHERE sChannelName=?", executeStr);
            
            data = cursor.fetchall();
            
            lastEndTime = 0;
            listing = None;
            
            for epgListing in epgListings:
                listing = Listing();
                
                listing.description = epgListing[5];
                listing.title = epgListing[3];
                listing.time = epgListing[6];
                listing.length = (epgListing[7] - listing.time) / 60;
                listing.content = "";
                listing.season = 0;
                listing.episode = 0;
                if data[0] != None:
                    listing.content = "pvr://channels/tv/All TV channels/" + str(data[0][0]) + ".pvr";                
                
                if listing.time - lastEndTime > 0 and lastEndTime != 0:
                    emptyListing = Listing()
                    emptyListing.description = "No Information Available";
                    emptyListing.title = "No Information Available";
                    emptyListing.time = lastEndTime;
                    emptyListing.length = (listing.time - lastEndTime) / 60;
                    emptyListing.content = "";
                    emptyListing.season = 0;
                    emptyListing.episode = 0;
                    emptyListing.content = listing.content;
                    self.listings.push(emptyListing);
                    
                self.listings.push(listing);
                    
                lastEndTime = epgListing[7];                
                
            emptyListing = Listing()
            emptyListing.description = "No Information Available";
            emptyListing.title = "No Information Available";
            emptyListing.time = lastEndTime;
            emptyListing.length = 60*60 * 24 * 5;
            emptyListing.content = "";
            emptyListing.season = 0;
            emptyListing.episode = 0;
            if listing != None:
                emptyListing.content = listing.content;
            self.listings.push(emptyListing);

            
        self.listings = self.listings.list;
        
        return self.listings;