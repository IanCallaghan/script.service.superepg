'''
Created on 7 Jul 2014

@author: Ian
'''
import os;
import xbmc;
import glob;
import sys;
import time;
from resources.lib.superepg.tools.array import Array;
from resources.lib.superepg.models.channel import Channel
from resources.lib.superepg.listers.liveTvLister import LiveTvLister
from resources.lib.superepg.livetv.livetvdbs import LiveTvDbs

class LiveTvGenerator(object):
    '''
    classdocs
    '''

    @staticmethod
    def getLiveChannels():
        
        cursor = LiveTvDbs.getDatabase(LiveTvDbs.EPGDB);
        cursor.execute("SELECT * FROM epg");
        epgListings = cursor.fetchall();
        channels = Array();
                
        liveNum = 0;
        for epgListing in epgListings:       
            liveChannel = Channel();
            liveChannel.id = liveNum;
            liveChannel.grabbers = [];
            liveChannel.filters = [];
            liveChannel.type = Channel.LIVE;
            liveChannel.lister = LiveTvLister(liveNum);
            liveChannel.create(time.time());
            liveChannel.name = liveChannel.lister.name;
            liveNum += 1; 
            
            channels.push(liveChannel);
            
        return channels.list;