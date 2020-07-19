import pickle
import numpy.testing
from pandas import testing
import numpy as np
from pandas.api.types import is_numeric_dtype, is_datetime64_dtype

class TestPlots():

    @classmethod
    def setup_class(self):
        with open('test_file/actual.pickle', 'rb') as file:
            self.actual = pickle.load(file)
        with open('question/plot1.pickle', 'rb') as file:
            self.plot1 = pickle.load(file)
        with open('question/plot2.pickle', 'rb') as file:
            self.plot2 = pickle.load(file)
        with open('question/plot3.pickle', 'rb') as file:
            self.plot3 = pickle.load(file)
        with open('question/plot4.pickle', 'rb') as file:
            self.plot4 = pickle.load(file)
    
    @classmethod
    def extract_axis(self, axes):
        return [ax.get_text() for ax in axes]

    def test_plot1_title(self):
        assert self.plot1.axes.get_title() == self.actual["plot1"]["plot1_title"]

    def test_plot1_y(self):
        assert self.extract_axis(list(self.plot1.axes.yaxis.get_ticklabels())) == self.actual["plot1"]["plot1_y"]

    def test_plot1_x(self):
        assert self.extract_axis(list(self.plot1.axes.xaxis.get_ticklabels())) == self.actual["plot1"]["plot1_x"]
    
    def test_plot1_height(self):
        assert self.plot1.figure.get_figheight() == self.actual["plot1"]["plot1_height"]
        
    def test_plot2_title(self):
        assert self.plot2.axes.get_title() == self.actual["plot2"]["plot2_title"]

    def test_plot2_y(self):
        assert self.extract_axis(list(self.plot2.axes.yaxis.get_ticklabels())) == self.actual["plot2"]["plot2_y"]

    def test_plot2_x(self):
        assert self.extract_axis(list(self.plot2.axes.xaxis.get_ticklabels())) == self.actual["plot2"]["plot2_x"]
    
    def test_plot2_height(self):
        assert self.plot2.figure.get_figwidth() == self.actual["plot2"]["plot2_width"]
        
    def test_plot3_x(self):
        assert self.extract_axis(list(self.plot3.axes.xaxis.get_ticklabels())) == self.actual["plot3"]["plot3_x"]
    
    def test_plot3_y(self):
        assert self.extract_axis(list(self.plot3.axes.yaxis.get_ticklabels())) == self.actual["plot3"]["plot3_y"]
    
    def test_plot3_bins(self):
        assert len(self.plot3.properties()["children"]) == self.actual["plot3"]["plot3_bin"]
    
    def test_plot3_width(self):
        assert self.plot3.figure.get_figwidth() == self.actual["plot3"]["plot3_width"]
    
    def test_plot3_title(self):
        assert self.plot3.axes.get_title() == self.actual["plot3"]["plot3_title"]
    
    def test_plot4_x(self):
        assert self.extract_axis(list(self.plot4.axes.xaxis.get_ticklabels())) == self.actual["plot4"]["plot4_x"]
    
    def test_plot4_width(self):
        assert self.plot4.figure.get_figwidth() == self.actual["plot4"]["plot4_width"]
    
    def test_plot4_title(self):
        assert self.plot4.axes.get_title() == self.actual["plot4"]["plot4_title"]
   
