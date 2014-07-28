'''
Created on 7 Jun 2014

@author: Ian
'''

class Cloner(object):
    '''
    classdocs
    '''

    @staticmethod
    def clone(dynOb, classOb):

        for x in dynOb:
            setattr(classOb, x, dynOb[x])

        return classOb