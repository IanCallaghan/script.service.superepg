'''
Created on 19 Jul 2014

@author: Ian
'''
class SpinControlOption(object):
    '''
    classdocs
    '''

    options = [];
    upBtn = None;
    downBtn = None;
    label = None;
    window = None;
    selectedIndex = 0;
    callback = None;
    
    def __init__(self, window, upId, downId, labelId, options, callback = None):
        self.options = options;
        self.window = window;
        
        self.upBtn = window.getControl(upId);
        self.downBtn = window.getControl(downId);
        self.label = window.getControl(labelId);
        self.callback = callback;
        
        self.setSelected();
        
        return;
    
    def setSelected(self):
        length = self.options.__len__();
        if self.selectedIndex < 0:
            self.selectedIndex = 0;
        if self.selectedIndex > length - 1:
            self.selectedIndex = length - 1;
            
        self.label.setLabel(self.options[self.selectedIndex]);
        
        if self.callback != None:
            self.callback();
        return;
    
    def setOptions(self, options):
        self.options = options;
        self.selectedIndex = 0;
        self.setSelected();
    
    def forwardInput(self, actionid):
        if actionid == 7:
            focusedItem = self.window.getFocus();
            
            if focusedItem == self.upBtn:
                self.selectedIndex -= 1;
                self.setSelected();
                
            if focusedItem == self.downBtn:
                self.selectedIndex += 1;
                self.setSelected();
                
        return;
    
    def getSelectedOption(self):
        return self.options[self.selectedIndex];
        