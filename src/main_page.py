
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
        plt.clf()
        training_set = []
        test_set = []
        split = 0.67
        k_nn.load_data_set(  split, constants.IRIS_DATA, training_set, test_set, )
        
        #plt.text(4 , 10, str('Train set: ' + repr(len(training_set))), size = 15)
        print 'Test set: ' + repr(len(test_set))
    	# generate predictions
        predictions = []
        k = 3
        colors = []
        for i in xrange(k):
            # set colors
            colors.append(((3 * (i + 1) % 11) / 11.0,
                             (7 * i % 11) / 11.0,
                             (9 * i % 11) / 11.0))
        plt.axis([10 ,80, 0, 60])
        for x in range(len(training_set)):
            
            if training_set[x][4] == 'Iris-setosa' :
                plt.plot(k_nn.hash_func(training_set[x][0],training_set[x][1]), k_nn.hash_func(training_set[x][2],training_set[x][3]), linestyle = 'None', marker = 'o', markersize = 5, color = colors[0])
            elif training_set[x][4] == 'Iris-versicolor':
                plt.plot(k_nn.hash_func(training_set[x][0],training_set[x][1]), k_nn.hash_func(training_set[x][2],training_set[x][3]), linestyle = 'None', marker = '<', markersize = 5, color = colors[1])
            else :
                plt.plot(k_nn.hash_func(training_set[x][0],training_set[x][1]), k_nn.hash_func(training_set[x][2],training_set[x][3]), linestyle = 'None', marker = 's', markersize = 5, color = colors[2])

                
        # plot knn
        for x in range(len(test_set)):
            neighbors = k_nn.get_neighbors(training_set, test_set[x], k)
            result = k_nn.get_class(neighbors)
            for y in range(0,k):
                if test_set[x][4] == 'Iris-setosa' :
                    plt.plot(k_nn.hash_func(test_set[x][0], test_set[x][1]), k_nn.hash_func(test_set[x][2], test_set[x][3]), linestyle = 'None', marker = 'o', markersize = 10, color = colors[0])
                elif test_set[x][4] == 'Iris-versicolor':
                    plt.plot(k_nn.hash_func(test_set[x][0], test_set[x][1]), k_nn.hash_func(test_set[x][2], test_set[x][3]), linestyle = 'None', marker = '<', markersize = 10, color = colors[1])
                else :
                    plt.plot(k_nn.hash_func(test_set[x][0], test_set[x][1]), k_nn.hash_func(test_set[x][2], test_set[x][3]), linestyle = 'None', marker = 's', markersize = 10, color = colors[2])
                print neighbors[y]
                
            predictions.append(result)
            print(' predicted=' + repr(result) + ', actual=' + repr(test_set[x][-1]))
        
        print "Accuracy = " + repr(k_nn.get_accuracy(test_set, predictions)) + "%"
        plt.show()        
        self 
        
    def push_naive_clicked(self):
        self 
        
    def push_kmeans_clicked(self):
        plt.clf()
        npoints = 100
        k = 7 # # clusters
        colors = []
        radius = 10
        points = k_means.generate_points(npoints, radius)
        cluster_centers = k_means.lloyd(points, k)
        for i in xrange(len(cluster_centers)):
            # set colors
            colors.append(((3 * (i + 1) % 11) / 11.0,
                             (7 * i % 11) / 11.0,
                             (9 * i % 11) / 11.0))
        # plot kmeans
        plt.axis([-radius, radius, -radius, radius])
        for i, cc in  enumerate(cluster_centers):
            plt.plot(cc.x, cc.y, linestyle = 'None', marker = '<', markersize = 10, color = colors[i])
            
            for p in points:
                
                if p.group != i:
                    continue
                plt.plot(p.x, p.y, linestyle = 'None', marker = 'o', color = colors[i])
                
        #plt.plot(cluster_x, cluster_y, linestyle = 'None', marker = '<', markerfacecolor = 'red')
        plt.show()
        #k_means.print_eps(points, cluster_centers)
        
        
    def push_fcm_clicked(self):
        self
        
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

