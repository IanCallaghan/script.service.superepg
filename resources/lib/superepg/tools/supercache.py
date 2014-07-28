'''
Created on 7 Jun 2014

@author: Ian
'''
from resources.lib.xbmctools.xbmcvideolibrary import VideoLibrary;

class LibraryCache(object):
    '''
    classdocs
    '''

    tvshows = None;
    movies = None;
    channels = None;
    episodeNames = [];
    episodes = None;
    episodeCount = 0;

    tvshowProps = ["title",
      "genre",
      "year",
      "rating",
      "plot",
      "studio",
      "mpaa",
      "cast",
      "playcount",
      "episode",
      "imdbnumber",
      "premiered",
      "votes",
      "lastplayed",
      "fanart",
      "thumbnail",
      "file",
      "originaltitle",
      "sorttitle",
      "episodeguide",
      "season",
      "watchedepisodes",
      "dateadded",
      "tag",
      "art"];

    ''''remove tag and cast fields they are super slow to fetch!'''
    tvshowPropsFast = ["title",
      "genre",
      #"year",
      #"rating",
      "plot",
      #"studio",
      #"mpaa",
      "playcount",
      #"episode",
      #"imdbnumber",
      #"premiered",
      #"votes",
      #"lastplayed",
      #"fanart",
      #"thumbnail",
      "file",
      #"originaltitle",
      #"sorttitle",
      #"episodeguide",
      #"season",
      #"watchedepisodes",
      #"dateadded",
      #"art"
      ];
      
    moviesProps = ["title", 
      "genre", 
      #"year", 
      #"rating", 
      #"director", 
      #"trailer", 
      #"tagline", 
      "plot", 
      #"plotoutline", 
      #"originaltitle", 
      #"lastplayed", 
      "playcount", 
      #"writer", 
      #"studio", 
      #"mpaa", 
      #"cast", 
      #"country", 
      #"imdbnumber", 
      "runtime", 
      #"set", 
      #"showlink", 
      #"streamdetails", 
      #"top250", 
      #"votes", 
      #"fanart", 
      #"thumbnail", 
      "file", 
      #"sorttitle", 
      #"resume", 
      #"setid", 
      #"dateadded", 
      #"tag", 
      #"art"
      ];

    episodePropsFast = ["title",
      "plot",
      #"votes",
      #"rating",
      #"writer",
      #"firstaired",
      "playcount",
      "runtime",
      #"director",
      #"productioncode",
      "season",
      "episode",
      #"originaltitle",
      #"showtitle",
      #"cast",
      #"streamdetails",
      #"lastplayed",
      #"fanart",
      #"thumbnail",
      "file",
      #"resume",
      #"tvshowid",
      #"dateadded",
      #"uniqueid",
      #"art"
      ];
      
    channelProps = ["thumbnail", 
      "channeltype", 
      "hidden", 
      "locked", 
      "channel", 
      "lastplayed"            
      ];


    @staticmethod
    def getChannels():
        if LibraryCache.channels is None:
            LibraryCache.channels = VideoLibrary.GetChannels("1", LibraryCache.channelProps, {})
        return LibraryCache.channels;
    
    @staticmethod
    def getTvShows():
        if LibraryCache.tvshows is None:
            LibraryCache.tvshows = VideoLibrary.GetTvShows(LibraryCache.tvshowPropsFast, {}, {})
        return LibraryCache.tvshows;
    
    @staticmethod
    def getMovies():
        if LibraryCache.movies is None:
            LibraryCache.movies = VideoLibrary.GetMovies(LibraryCache.moviesProps, {}, {})
        return LibraryCache.movies;

    @staticmethod
    def getEpisodes(tvShowId, season = None):
        if LibraryCache.episodes is None:
            LibraryCache.episodes = [];
            LibraryCache.episodeNames = [];


        i = 0;
        index = -1;
        for ep in LibraryCache.episodeNames:
            if ep == tvShowId:
                index = i;
            i = i + 1;

        if index != -1:
            return LibraryCache.episodes[index];

        episodes = VideoLibrary.GetEpisodes(tvShowId, season, LibraryCache.episodePropsFast, {}, {});
        LibraryCache.episodeNames.insert(LibraryCache.episodeCount, tvShowId)
        LibraryCache.episodeCount = LibraryCache.episodeCount + 1;
        LibraryCache.episodes.insert(LibraryCache.episodeCount, episodes);

        return episodes
