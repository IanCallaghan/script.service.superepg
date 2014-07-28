'''
Created on 2 Jul 2014

@author: Ian
'''
class ListingView(object):
    '''
    classdocs
    '''
    width = 0;
    x = 0;
    y = 0;
    visible = True;
    button = None;
    
    def remove(self):
        return;
    
    def setPos(self, x, y):
        self.x = x;
        self.y = y;