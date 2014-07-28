'''
Created on 6 Jun 2014

@author: Ian
'''

import json
import xbmc
import sys;
import time;
from resources.lib.tools.reflection import Reflection

class JsonQuery(object):

    jsonOb = {}
    def __init__(self, method, params):
        '''
        Constructor
        '''
        self.jsonOb = {"jsonrpc"     : "2.0",'id': 1, "method": method,
                       "params"      : params}

    def query(self, ret):
        try:
            xbmc_request = json.dumps(self.jsonOb)
            result = xbmc.executeJSONRPC(xbmc_request)
            if ret:
                return json.loads(result)['result']
            else:
                return json.loads(result)
        except:
            return
        return

    @staticmethod
    def doQuery(method, props, names, ret = True):
        sys.stdout.write("Json Query - " + method + " params:" + str(props) + "\n");
        timeNow = time.time();
        params = Reflection.groupSetNonNull(props, names);
        json = JsonQuery(method, params);
        jsonOb = json.query(ret);
        timeDiff = time.time() - timeNow;
        sys.stdout.write("Took: " + str(timeDiff) + "\n");
        return jsonOb;