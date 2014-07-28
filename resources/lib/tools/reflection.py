'''
Created on 7 Jun 2014

@author: Ian
'''

from resources.lib.xbmctools.xbmcnotifications import Notifier

class Reflection(object):
    '''
    classdocs
    '''

    @staticmethod
    def listProps(ob):
        i = 10;
        for x in ob:
            i += 10
            Notifier.notify(x, i)
        return {}

    @staticmethod
    def groupSetNonNull(props, names):
        ob = {}
        i = 0
        for x in names:
            Reflection.setNoneNull(ob, props[i], names[i])
            i = i + 1
        return ob

    @staticmethod
    def setNoneNull(ob, prop, name):
        if prop != None:
            ob[name] = prop
        return ob
