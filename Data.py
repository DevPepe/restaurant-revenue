'''
This class handle the raw data
'''
import sys 
class Data():
    data = []

    def __init__(self, csv):
        flag = True

        def getRevenue(row):
            row[len(row) - 1] = row[len(row) - 1].replace('\n', '')
            return row

        def toFloat(row):
            # Cast P1:P37 and revenue to float
            for i in xrange(5, len(row)):
                row[i] = float(row[i])
            return row

        def utf8ToAscii(row):
            # City name from UTF-8 to ASCII
            row[2] = row[2].decode('utf-8')
            row[2] = row[2].encode('ascii', 'ignore')
            return row

        def parseDate(row):
            # Remove date
            date = row.pop(1).split('/')
            row.insert(1, int(date[2]))
            row.insert(1, int(date[1]))
            return row

        with open(csv, 'r+') as f:
            for line in f:
                # Discard the first line
                if (flag == False):
                    row = line.split(',')
                    row = getRevenue(row)
                    row = toFloat(row)
                    row = utf8ToAscii(row)
                    row = parseDate(row)
                    self.data.append(row)
                else: 
                    flag = False 
	                               
    
    def load(self, file):
        print '\n Loading data from a pickle file into Numpy arrays'

    # Check min and max revenues in training data
    def getLimits(self):
        min = sys.maxint
        max = 0

    	for i in xrange(len(self.data)):
    		revenue = int(self.data[i][len(self.data[i]) - 1])
    		if (revenue < min):
    			min = revenue
    		elif (revenue > max):
    			max = revenue

    	print 'The min revenue is {0} and the max is {1}' .format(min, max)




    	


if __name__ == "__main__":
    d = Data("/Users/Navarro/Documents/Kaggle_Competition/Restaurant_Revenue_Prediction/restaurant-revenue/Data/train.csv")
    d.getLimits()



