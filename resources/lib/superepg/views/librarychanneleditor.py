'''
Created on 15 Jul 2014

@author: Ian
'''

import xbmcgui;
import xbmcaddon;
from resources.lib.xbmctools.xbmcactions import XbmcActions
from resources.lib.superepg.views.spincontroloption import SpinControlOption
from resources.lib.superepg.grabbers.randomGrabber import RandomGrabber
from resources.lib.superepg.tools.array import Array
from resources.lib.superepg.grabbers.unwatchedOnlygrabber import UnwatchedOnlyGrabber
from resources.lib.superepg.listers.inOrderTvLister import InOrderTvLister
from resources.lib.superepg.listers.inOrderMovieLister import InOrderMovieLister
from resources.lib.superepg.listers.randomMovieLister import RandomMovieLister
from resources.lib.superepg.filters.genreFilter import GenreFilter
from resources.lib.superepg.filters.nameFilter import NameFilter
from resources.lib.superepg.filters.filterTypes import FilterTypes
from resources.lib.superepg.models.channel import Channel
from resources.lib.superepg.tools.serialiser import Serialiser

class LibraryChannelEditor(xbmcgui.WindowXML):
    '''
    classdocs
    '''
    
    DETAILS_NAME = 103;
    
    GRABBERS_PRIMARY_OPTIONS = 203;
    GRABBERS_PRIMARY_DOWN = 204;
    GRABBERS_PRIMARY_UP = 205;
    
    GRABBERS_SECONDARY_OPTIONS = 208;
    GRABBERS_SECONDARY_DOWN = 209;
    GRABBERS_SECONDARY_UP = 210;
    
    FILTERS_LIST = 301;
    
    LISTERS_MAX = 403;
    LISTERS_MOVIE = 406;
    
    LISTERS_TV_OPTIONS = 409;
    LISTERS_TV_DOWN = 410;
    LISTERS_TV_UP = 411;
    
    LISTERS_MOVIE_OPTIONS = 414;
    LISTERS_MOVIE_DOWN = 415;
    LISTERS_MOVIE_UP = 416;
    
    EDITOR_NAME = 503;
    
    EDITOR_TYPE_OPTIONS = 506;
    EDITOR_TYPE_DOWN = 507;
    EDITOR_TYPE_UP = 508;
    
    EDITOR_CONNECTOR_OPTIONS = 511;
    EDITOR_CONNECTOR_DOWN = 512;
    EDITOR_CONNECTOR_UP = 513;
    
    EDITOR_OPTION_OPTIONS = 516;
    EDITOR_OPTION_DOWN = 517;
    EDITOR_OPTION_UP = 518;
    
    EDITOR_TVMOVIE_OPTIONS = 523;
    EDITOR_TVMOVIE_DOWN = 524;
    EDITOR_TVMOVIE_UP = 525;
    
    EDITOR_CANCEL = 519
    EDITOR_SUBMIT = 520;
    
    MASTER_CANCEL = 600;
    MASTER_SUBMIT = 601;
    
    channelManager = None;
    channelMenu = None;
    
    detailsNameTxt  = None;    
    
    grabbersPrimaryToggle = None;
    grabbersSecondaryToggle = None;
    
    filtersList = None;
    
    listersMaxTxt = None;
    listersMovieTxt = None;
    listersTvToggle = None;
    listersMoviesToggle = None;
    
    editorNameTxt = None;
    editorTypeToggle = None;
    editorConnectorToggle = None;
    editorOptionToggle = None;
    editorTvMovieToggle = None;
    editorCancelBtn = None;
    editorSubmitBtn = None;
    
    submitBtn = None;
    cancelBtn = None;
    
    inputForwardControls = [];
    
    grabbers = [];
    tvListers = [];
    movieListers = [];
    filterers = [];
    connectors = [];
    options = [];
    tvMovieTypes = [];
    filtersCreated = [];
    
    def __new__(cls):
        ADDON = xbmcaddon.Addon(id = 'script.service.superepg')
        return super(LibraryChannelEditor, cls).__new__(cls, 'librarychanneleditor.xml', ADDON.getAddonInfo('path'));

    def __init__(self):
        super(LibraryChannelEditor, self).__init__();
        
        
    def onInit(self):      
                
        self.filtersCreated = [];
        self.grabbers = [UnwatchedOnlyGrabber(), RandomGrabber()];
        grabberNames = Array();
        for grabber in self.grabbers:
            grabberNames.push(grabber.getName());
            
        self.tvListers = [InOrderTvLister(0,0,None)];
        tvListerNames = Array();
        for lister in self.tvListers:
            tvListerNames.push(lister.getName());
            
        self.movieListers = [InOrderMovieLister(0), RandomMovieLister(0)];
        movieListerNames = Array();
        for lister in self.movieListers:
            movieListerNames.push(lister.getName());
            
        self.filterers = [GenreFilter([], ""), NameFilter([], "")];
        filterNames = Array();
        for fil in self.filterers:
            filterNames.push(fil.getName());
            
        self.connectors = [FilterTypes.NO_CONNECTOR, FilterTypes.AND_CONNECTOR, FilterTypes.OR_CONNECTOR];
        self.tvMovieTypes = [FilterTypes.TV_FILTER, FilterTypes.MOVIE_FILTER];
            
        self.detailsNameTxt = self.getControl(self.DETAILS_NAME);
            
        self.grabbersPrimaryToggle = SpinControlOption(self, self.GRABBERS_PRIMARY_UP, self.GRABBERS_PRIMARY_DOWN, self.GRABBERS_PRIMARY_OPTIONS, grabberNames.list);
        self.grabbersSecondaryToggle = SpinControlOption(self, self.GRABBERS_SECONDARY_UP, self.GRABBERS_SECONDARY_DOWN, self.GRABBERS_SECONDARY_OPTIONS, grabberNames.list);
        
        self.filtersList = self.getControl(self.FILTERS_LIST);
        
        self.listersMaxTxt = self.getControl(self.LISTERS_MAX);
        self.listersMovieTxt = self.getControl(self.LISTERS_MOVIE);        
        self.listersTvToggle = SpinControlOption(self, self.LISTERS_TV_UP, self.LISTERS_TV_DOWN, self.LISTERS_TV_OPTIONS, tvListerNames.list);
        self.listersMoviesToggle = SpinControlOption(self, self.LISTERS_MOVIE_UP, self.LISTERS_MOVIE_DOWN, self.LISTERS_MOVIE_OPTIONS, movieListerNames.list);
        
        self.editorNameTxt = self.getControl(self.EDITOR_NAME);
        self.editorTvMovieToggle = SpinControlOption(self, self.EDITOR_TVMOVIE_UP, self.EDITOR_TVMOVIE_DOWN, self.EDITOR_TVMOVIE_OPTIONS, self.tvMovieTypes, self.onFilterTypeChange);
        self.editorTypeToggle = SpinControlOption(self, self.EDITOR_TYPE_UP, self.EDITOR_TYPE_DOWN, self.EDITOR_TYPE_OPTIONS, filterNames.list, self.onFilterTypeChange);
        self.editorConnectorToggle = SpinControlOption(self, self.EDITOR_CONNECTOR_UP, self.EDITOR_CONNECTOR_DOWN, self.EDITOR_CONNECTOR_OPTIONS, self.connectors);
        self.editorOptionToggle = SpinControlOption(self, self.EDITOR_OPTION_UP, self.EDITOR_OPTION_DOWN, self.EDITOR_OPTION_OPTIONS, [""]);
        self.editorCancelBtn = self.getControl(self.EDITOR_CANCEL);
        self.editorSubmitBtn = self.getControl(self.EDITOR_SUBMIT);
        
        self.cancelBtn = self.getControl(self.MASTER_CANCEL);
        self.submitBtn = self.getControl(self.MASTER_SUBMIT);
        
        self.filtersList.addItem(xbmcgui.ListItem("New", "No Connector"));
        
        self.inputForwardControls = [self.grabbersPrimaryToggle, self.grabbersSecondaryToggle, self.listersTvToggle, self.listersMoviesToggle,
                                     self.editorTypeToggle, self.editorConnectorToggle, self.editorOptionToggle, self.editorTvMovieToggle];
        
        self.setFocus(self.detailsNameTxt);
        
        self.grabbersSecondaryToggle.selectedIndex = 1;
        self.grabbersSecondaryToggle.setSelected();
        self.listersMoviesToggle.selectedIndex = 1;
        self.listersMoviesToggle.setSelected();
        self.listersMaxTxt.setText("100");
        self.listersMovieTxt.setText("5")
        
        self.onFilterTypeChange();
        
        return;
    
    def onFilterTypeChange(self):
        if self.editorTvMovieToggle == None or self.editorTypeToggle == None:
            return;
        filterTvType = self.editorTvMovieToggle.getSelectedOption();
        filterType = self.editorTypeToggle.getSelectedOption();
        
        for filter in self.filterers:
            if filter.getName() == filterType:
                self.options = filter.getOptions(filterTvType);
                
        self.editorOptionToggle.setOptions(self.options);
        return;
    
    def addFilter(self):
        filterName = self.editorTypeToggle.getSelectedOption();
        params = [self.editorOptionToggle.getSelectedOption()];
        connectorType = self.editorConnectorToggle.getSelectedOption();
        filterType = self.editorTvMovieToggle.getSelectedOption();
        
        newFilter = None;
        
        if filterName == GenreFilter([],"").getName():
            newFilter = GenreFilter(params, filterType, connectorType, True);
            
        if newFilter != None:
            newFilter.label = self.editorNameTxt.getText();
            self.filtersCreated.insert(self.filtersCreated.__len__()-1, newFilter);
            self.filtersList.addItem(xbmcgui.ListItem(newFilter.label, newFilter.connectorType));
        
        return;
            
    
    def onAction(self, action):
        focusedItem = self.getFocus();
        actionid = action.getId();
        
        if action.getId() == XbmcActions.KEY_NAV_BACK:
            self.close();
        if action.getId() == XbmcActions.ACTION_SELECT_ITEM:
            if focusedItem == self.cancelBtn:
                self.close();
            if focusedItem == self.submitBtn:
                self.createChannel();
            if focusedItem == self.editorSubmitBtn:
                self.addFilter();
        
        for control in self.inputForwardControls:
            control.forwardInput(action.getId());
        return;
    
    def createChannel(self):
        
        channel = Channel()
        channel.name = self.detailsNameTxt.getText();
        
        grabbers = [];
        for grabber in self.grabbers:
            if grabber.getName() == self.grabbersPrimaryToggle.getSelectedOption():
                if grabber.getName() == UnwatchedOnlyGrabber().getName():
                    grabbers.insert(0, UnwatchedOnlyGrabber());
                if grabber.getName() == RandomGrabber().getName():
                    grabbers.insert(0, RandomGrabber());
                    
        for grabber in self.grabbers:
            if grabber.getName() == self.grabbersSecondaryToggle.getSelectedOption():
                if grabber.getName() == UnwatchedOnlyGrabber().getName():
                    grabbers.insert(1, UnwatchedOnlyGrabber());
                if grabber.getName() == RandomGrabber().getName():
                    grabbers.insert(1, RandomGrabber());
                
        
        channel.grabbers = grabbers;
        
        maxListers = int(self.listersMaxTxt.getText());
        movieEvery = int(self.listersMovieTxt.getText());
        movieLister = None;
        tvLister = None;
        
        if self.listersMoviesToggle.getSelectedOption() == InOrderMovieLister(0).getName():
            movieLister = InOrderMovieLister(maxListers);
        if self.listersMoviesToggle.getSelectedOption() == RandomMovieLister(0).getName():
            movieLister = RandomMovieLister(maxListers);
            
        if self.listersTvToggle.getSelectedOption() == InOrderTvLister(0,0,None).getName():
            tvLister = InOrderTvLister(maxListers, movieEvery, movieLister);
            
        channel.lister = tvLister;
        channel.filters = self.filtersCreated;
        channel.create(self.channelManager.timeNow);
        channel.refreshGrabbers();
        self.channelManager.channels.insert(self.channelManager.channels.__len__()-1, channel);
        self.channelManager.save();
        
        self.close();
        
        return;
        