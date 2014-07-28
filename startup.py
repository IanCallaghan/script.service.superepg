'''
Created on 28 Jun 2014

@author: Ian

Entry Point for system startup
'''
import xbmc;
from resources.lib.superepg.controllers.mainManager import MainManager

MainManager.start();

while not xbmc.abortRequested:
        xbmc.sleep(10000);
