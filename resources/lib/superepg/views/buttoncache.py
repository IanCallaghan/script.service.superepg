'''
Created on 11 Jul 2014

@author: Ian
'''
from resources.lib.superepg.tools.superchannel import EpgButton

class ButtonCache(object):
    '''
    classdocs
    '''

    buttons = [];
    index = 0;
    winow = None;

    def __init__(self, window):
        '''
        Constructor
        '''
        self.window = window;
        self.buttons.insert(0, None)
        return;
    
    def clear(self):
        self.index = 0;
        for button in self.buttons:
            if button != None:
                return;#button.setVisible(False);
        return;
    
    def postCleanup(self):
        i = 0;
        for button in self.buttons:
            if i >= self.index and button != None:
                button.setVisible(False);
            i += 1;
        return;
        
    def getNextButton(self):
        if self.buttons[self.index] == None:
            self.buttons[self.index] = EpgButton.getBtn(0, 0, 10, 10, "", False);
            self.window.addControl(self.buttons[self.index]);
            self.index += 1;
            self.buttons.insert(self.index, None);
            return self.buttons[self.index-1];
        self.index += 1;        
        #self.buttons[self.index].setVisible(True);
        return self.buttons[self.index-1];
            
            
        