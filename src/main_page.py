
import sys
import k_nn
import k_means
import constants

import matplotlib.pyplot as plt
from PyQt4 import QtCore, QtGui, uic
first_page = uic.loadUiType("../ui/first_page.ui")[0]
class MyWindowClass(QtGui.QMainWindow, first_page):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.setupUi(self)
        self.push_knn.clicked.connect(self.push_knn_clicked)  # Bind the event handlers
        self.push_naive.clicked.connect(self.push_naive_clicked)  #   to the buttons
        self.push_kmeans.clicked.connect(self.push_kmeans_clicked)
        self.push_fcm.clicked.connect(self.push_fcm_clicked)

        self.menuHelp.addAction('&About', self.about)  # add About to Help
        self.statusBar().showMessage("Start Page")
        self.statusBar().setSizeGripEnabled(False)
        

    def about(self):
        QtGui.QMessageBox.about(self, "About",constants.ABOUT_MESSAGE)
    
    def push_knn_clicked(self):
        training_set=[]
        test_set=[]
        split = 0.67
        k_nn.load_data_set(  split, constants.IRIS_DATA, training_set, test_set, )
        
        plt.text(4 , 10, str('Train set: ' + repr(len(training_set))), size = 15)
        print 'Test set: ' + repr(len(test_set))
    	# generate predictions
        predictions=[]
        k = 3
        for x in range(len(test_set)):
            neighbors = k_nn.get_neighbors(training_set, test_set[x], k)
            result = k_nn.get_class(neighbors)
            for y in range(0,k):
                print neighbors[y]
            predictions.append(result)
            #print('> predicted=' + repr(result) + ', actual=' + repr(test_set[x][-1]))
    	
        plt.show()        
        self 
        
    def push_naive_clicked(self):
        self 
        
    def push_kmeans_clicked(self):
        npoints = 30000
        k = 7 # # clusters
        points = k_means.generate_points(npoints, 10)
        cluster_centers = k_means.lloyd(points, k)
        #k_means.print_eps(points, cluster_centers)
        
        
    def push_fcm_clicked(self):
        self
        

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()

app.exec_()
