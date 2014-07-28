'''
Created on 6 Jun 2014

@author: Ian
'''
from resources.lib.xbmctools.xbmcjsonquery import JsonQuery
from resources.lib.tools.clonetools import Cloner

class VideoLibrary(object):
    '''
    classdocs
    '''

    @staticmethod
    def GetMovies(properties = None, limits = None, sort = None, filterOb = None):
        '''[ Video.Fields.Movie properties ] [ List.Limits limits ] [ List.Sort sort ] [ mixed filter ]'''
        method = "VideoLibrary.GetMovies"
        props = [properties, limits, sort, filterOb];
        names = ["properties", "limits", "sort", "filter"];
        return GetMoviesObject(JsonQuery.doQuery(method, props, names));

    @staticmethod
    def GetTvShows(properties = None, limits = None, sort = None, filterOb = None):
        '''[ Video.Fields.TVShow properties ] [ List.Limits limits ] [ List.Sort sort ] [ mixed filter ]'''
        method = "VideoLibrary.GetTVShows";
        props = [properties, limits, sort, filterOb];
        names = ["properties", "limits", "sort", "filter"];
        return GetTvShowsObject(JsonQuery.doQuery(method, props, names));

    @staticmethod
    def GetEpisodes(tvshowid, season = None, properties = None, limits = None, sort = None, filterOb = None):
        '''[ Library.Id tvshowid = -1 ] [ integer season = -1 ] [ Video.Fields.Episode properties ] [ List.Limits limits ] [ List.Sort sort ] [ mixed filter ]'''
        method = "VideoLibrary.GetEpisodes";
        props = [tvshowid, season, properties, limits, sort, filterOb];
        names = ["tvshowid", "season", "properties", "limits", "sort", "filter"];
        return GetEpisodesObject(JsonQuery.doQuery(method, props, names));
    
    @staticmethod
    def GetChannels(channelgroupid, properties = None, limits = None):
        '''PVR.ChannelGroup.Id channelgroupid [ PVR.Fields.Channel properties ] [ List.Limits limits ]'''
        method = "PVR.GetChannels";
        props = [channelgroupid, properties, limits];
        names = ["channelgroupid", "properties", "limits"];
        return GetChannelsObject(JsonQuery.doQuery(method, props, names));
    
    @staticmethod
    def GetGenres(typeName, properties = None, limits = None, sort = None):
        '''string type [ Library.Fields.Genre properties ] [ List.Limits limits ] [ List.Sort sort ]'''
        method = "VideoLibrary.GetGenres";
        props = [typeName, properties, limits, sort];
        names = ["type", "properties", "limits", "sort"];
        return GetGenresObject(JsonQuery.doQuery(method, props, names));
    

class GetChannelsObject(object):
    '''List.LimitsReturned limits PVR.Details.Channel[] channels'''
    channels = [];
    limits = {};

    def __init__(self, jsonOb):
        Cloner.clone(jsonOb, self);

class GetMoviesObject(object):
    '''List.LimitsReturned limits [ Video.Details.Movie[] movies ]'''
    movies = [];
    limits = {};

    def __init__(self, jsonOb):
        Cloner.clone(jsonOb, self);

class GetTvShowsObject(object):
    '''List.LimitsReturned limits [ Video.Details.TVShow[] tvshows ]'''
    tvshows = [];
    limits = {};

    def __init__(self, jsonOb):
        Cloner.clone(jsonOb, self);

class GetEpisodesObject(object):
    '''[ Video.Details.Episode[] episodes ] List.LimitsReturned limits'''
    episodes = [];
    limits = {};

    def __init__(self, jsonOb):
        Cloner.clone(jsonOb, self);

class GetGenresObject(object):
    '''List.LimitsReturned limits [ Video.Details.Movie[] movies ]'''
    genres = [];
    limits = {};

    def __init__(self, jsonOb):
        Cloner.clone(jsonOb, self);
