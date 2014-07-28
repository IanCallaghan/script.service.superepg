'''
Created on 9 Jun 2014

@author: Ian
'''

class Array(object):
    '''
    classdocs
    '''

    list = [];
    count = 0;

    def __init__(self):
        self.list = [];
        self.count = 0;

    def push(self, ob):
        self.list.insert(self.count, ob);
        self.count = self.count + 1;