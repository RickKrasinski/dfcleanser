

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random


def fix_ipython():
    from IPython import get_ipython
    ipython = get_ipython()
    if ipython is not None:
        ipython.magic("gui qt5")


import logging
logger = logging.getLogger(__name__)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

# Set the exception hook to our wrapping function
sys.excepthook = except_hook

# Enables PyQt event loop in IPython
fix_ipython()



class GraphsGui(QtWidgets.QMainWindow):

    def __init__(self, dfparms, **kwargs):

        # Enables PyQt event loop in IPython
        fix_ipython()  

        # create the app for uniques
        from PyQt5.QtCore import QCoreApplication

        self.app = QCoreApplication.instance()
        if(self.app is None) :
            self.app = QtWidgets.QApplication(sys.argv) 

        # release resources on close
        self.app.setQuitOnLastWindowClosed(True)  

        super().__init__()

        self.left = 100
        self.top = 100
        self.title = 'dfcleanser column graphs'
        self.width = 800
        self.height = 600

        self.dftitle    =   dfparms[0]
        self.colname    =   dfparms[1]
        self.graphid    =   dfparms[2]

        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        m = PlotCanvas(self, width=5, height=4, dftitle=self.dftitle, colname=self.colname, graphid=self.graphid)
        m.move(0,0)
        #self.show()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dftitle=None, colname=None, graphid=None, dpi=100):

        print("PlotCanvas",dftitle, colname, graphid)

        fig = Figure(figsize=(8,6))#(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        if(graphid == 0) :
            self.display_histogram_graph(dftitle,colname)
        elif(graphid == 1) :   
            self.display_zscores_graph(dftitle,colname)
        elif(graphid == 2) :   
            self.display_heat_map_graph(dftitle,colname)
        elif(graphid == 3) :   
            self.display_box_plot_graph(dftitle,colname)

    def plot(self):

        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt and Matplotlib Demonstration')
        self.draw()
    
    def display_histogram_graph(self,dftitle,colname) :

        print("display_histogram_graph",dftitle, colname)

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(dftitle)

        import numpy as np
        counts      =   df[colname].value_counts().to_dict()
        dfuniques   =   list(counts.keys())
        uniques     =   np.asarray(dfuniques)
        ucounts     =   list(counts.values())
        ucounts     =   np.asarray(ucounts)

        import matplotlib.pyplot as plt

        ax = self.figure.add_subplot(111)
        ax.hist(uniques,weights=ucounts)
        ax.set_title("'" + colname + "'" + " Histogram")
        self.draw()


    def calculate_column_zscores(self,df,colname) :
    
        import numpy as np

        counts      =   df[colname].value_counts().to_dict()
        dfuniques   =   list(counts.keys())
        uniques     =   np.asarray(dfuniques)
        ucounts     =   list(counts.values())
        ucounts     =   np.asarray(ucounts)

        cmean       =   df[colname].mean() 
        cstd        =   df[colname].std()

        zscores      =   []
        for i in range(len(dfuniques)) :
            zscores.append((dfuniques[i]-cmean)/cstd)
        
        # dictionary of lists  
        zdict = {'ZScore': zscores, 'Frequency': ucounts}  

        return(zdict)

    def display_zscores_graph(self,dftitle,colname):

        #dftitle = "Crime_Scenes"
        #colname = "Area ID"

        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(dftitle)

        zdict   =   self.calculate_column_zscores(df,colname)
    
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        zdf     =   pd.DataFrame(zdict) 

        ax = self.figure.add_subplot(111)
        sns.kdeplot(df[colname],bw_method=3,ax=ax)
        ax.set_title("'" + colname + "'" + " ZScores")
        self.draw()


    def display_heat_map_graph(self,dftitle,colname) :

        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
    
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(dftitle)

        col_uniques     =   df[colname].unique().tolist()
        col_counts      =   df[colname].value_counts().tolist()

        graph_uniques   =   []
        graph_counts    =   []
        for i in range(len(col_uniques)) :
            if(not(pd.isnull(col_uniques[i]))) :
                graph_uniques.append(col_uniques[i])
                graph_counts.append(df[colname].value_counts()[col_uniques[i]])

        graphdf = pd.DataFrame({colname: graph_uniques},index=graph_counts)

        ax = self.figure.add_subplot(111)
        sns.heatmap(graphdf, annot=True, fmt="g", cmap='viridis',ax=ax)
        ax.set_title("'" + colname + "'" + " HeatMap")
        self.draw()
        
    def display_box_plot_graph(self,dftitle,colname) :

        # Import libraries
        import matplotlib.pyplot as plt
        import numpy as np
        import seaborn as sns
    
        from dfcleanser.common.cfg import get_dfc_dataframe_df
        df  =   get_dfc_dataframe_df(dftitle)
 
        ax = self.figure.add_subplot(111)
        fig = plt.figure(figsize =(10, 7))
        sns.boxplot(data=df,x=colname,ax=ax)

        ax.set_title("'" + colname + "'" + " BoxPlot")
        self.draw()



# -----------------------------------------------------------------#
# -                Global access to display graphs                -#
# -----------------------------------------------------------------#
def showdfcGraph(dftitle,colname,graphid)  :

    print("showdfcGraph",dftitle,colname,graphid)

    dfcGraph_gui = GraphsGui([dftitle,colname,int(graphid)])
    print("dfcGraph_gui show",dftitle,colname,graphid)
    dfcGraph_gui.show()

    return dfcGraph_gui 

#if __name__ == '__main__':##


    #app = QApplication(sys.argv)
    #ex = App()
    #sys.exit(app.exec_())
