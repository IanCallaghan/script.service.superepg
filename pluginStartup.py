'''
Created on 28 Jun 2014

@author: Ian

Entry point for gui plugin
'''
from resources.lib.superepg.controllers.mainManager import MainManager;

'''
Need a way to access the data from the service,
perhaps need to use an sqllite database, this may be required for perm storage anyway :(
'''

MainManager.startGui();