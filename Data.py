'''
This class extract the data from the csv files
to numpy arrays
'''

class Data():
    
    def dump(self, file):
    	print '\n Dumping the data from {0} into a pickle' .format(file)
    
    def load(self, file):
        print '\n Loading data from a pickle file into Numpy arrays'


