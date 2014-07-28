'''
Created on 7 Jul 2014

@author: Ian
'''
import sys;
import os;
import glob;
import xbmc;
from resources.lib.superepg.tools.array import Array

class LiveTvDbs(object):
    '''
    classdocs
    '''

    TVDB = "TV";
    EPGDB = "Epg";
    
    @staticmethod
    def getDatabase(dbName):
        try:
            from sqlite3 import dbapi2 as sqlite3;
        except ImportError:
                sys.stderr.write("Error: " +
                    "sql failed");
                    
        profilePath = LiveTvDbs.getDatabaseDir();
        
        files = Array();
        if os.path.exists(profilePath):
            for nFile in glob.glob1(profilePath, "*.db"):
                if nFile.find(dbName) != -1:
                    files.push(nFile);
                    
            highestDbNum = -1;
            highestDbFile = "";
            for nFile in files.list:
                finalFile = nFile.split(dbName)[1];
                finalFile = finalFile.split(".db")[0];
                finalFileNum = int(finalFile);
                if finalFileNum > highestDbNum:
                    highestDbNum = finalFileNum;
                    highestDbFile = nFile;
        
        conn = sqlite3.connect(profilePath + highestDbFile);
        return conn.cursor();
            
    @staticmethod
    def getDatabaseDir():
        return xbmc.translatePath(os.path.join('special://userdata/Database', ''));