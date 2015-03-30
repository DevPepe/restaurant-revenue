'''
This class preprocess the data
'''

from data import Data

class Preprocess():

	def __init__(self):
		d = Data()
		d.load('data.pkl');
	
	# Standarization
	def standar(self):
		pass
	# Normalization	
	def norm(self):
	    pass


if __name__ == "__main__":
	p = Preprocess()