'''
Created on 7 Jun 2014

@author: Ian
'''
import xbmcgui;
import xbmcaddon;

class EpgButton(object):
    
    
    @staticmethod
    def getBtn(x, y, width, height, label, add=False):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        path = ADDON.getAddonInfo('path');
        skinPath = "\\resources\\skins\\Default\\media"
        texture = path + skinPath +"\\tvguide-program.png";
        focusTexture = path + skinPath + "\\tvguide-program-focus.png";
        return xbmcgui.ControlButton(x, y, width, height, label, focusTexture=focusTexture, noFocusTexture=texture, alignment=4, font="font10", textColor="ffffffff");

    @staticmethod
    def getChannelBtn(x, y, width, height, label, add=False):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        path = ADDON.getAddonInfo('path');
        skinPath = "\\resources\\skins\\Default\\media"
        texture = path + skinPath +"\\tvguide-channel.png";
        focusTexture = path + skinPath + "\\tvguide-channel.png";
        return xbmcgui.ControlButton(x, y, width, height, label, focusTexture=focusTexture, noFocusTexture=texture, alignment=4, font="font10", textColor="ffffffff");

    @staticmethod
    def getTimeBarImg(x, y, width, height):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        path = ADDON.getAddonInfo('path');
        skinPath = "\\resources\\skins\\Default\\media"
        texture = path + skinPath +"\\tvguide-timebar.png";
        return xbmcgui.ControlImage(x, y, width, height, texture);

