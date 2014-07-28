'''
Created on 6 Jun 2014

@author: Ian
'''

import xbmcaddon
import xbmc

class Notifier(object):
    '''
    classdocs
    '''

    @staticmethod
    def notify(text, delay):
        __addon__       = xbmcaddon.Addon()
        __addonname__   = __addon__.getAddonInfo('name')
        __icon__        = __addon__.getAddonInfo('icon')
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__, text, delay, __icon__))
        return {}
