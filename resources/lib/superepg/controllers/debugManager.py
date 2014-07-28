'''
Created on 21 Jun 2014

@author: Ian
'''
import sys;

class DebugManager(object):
    '''
    classdocs
    '''


    def __init__(self, debug = True):
        '''
        Constructor
        '''
        if debug:
            # Make pydev debugger works for auto reload.
            # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
            try:
                from pysrc import pydevd;  
            except:
                sys.stderr.write("Error: " +
                    "You must add org.python.pydev.debug.pysrc to your PYTHONPATH.");
                return;
            
            try:
                pydevd.settrace("localhost", stdoutToServer=True, stderrToServer=True, suspend=True);
            except:
                sys.stderr.write("Error: " +
                    "You must add org.python.pydev.debug.pysrc to your PYTHONPATH.");
                return;