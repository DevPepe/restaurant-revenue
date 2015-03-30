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
            row.insert(1, int(date[0]))
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

    # Check min and max revenues in training data
    def getLimitRevenue(self):
        min = sys.maxint
        max = 0

    	for i in xrange(len(self.data)):
    		revenue = int(self.data[i][len(self.data[i]) - 1])
    		if (revenue < min):
    			min = revenue
    		elif (revenue > max):
    			max = revenue
        
    	print 'The min revenue is {0} and the max is {1}' .format(min, max)

    # Show when the last restaurant was open
    def getOpenDate(self, limit):
        
        def getIndex(index):
        	return self.data[index][2], self.data[index][1]
        
        def getNewst():
        	year = 0
        	month = 0

    		for i in xrange(len(self.data)):
    			index_year, index_month = getIndex(i)
	    		
	    		if (index_year > year):
	    				year, month = index_year, index_month

    			elif (index_year == year) and (index_month >= month):
    				year, month = index_year, index_month

	    	return year, month

    	def getOldest():
    		year = sys.maxint
    		month = sys.maxint

    		for i in xrange(len(self.data)):
    			index_year, index_month = getIndex(i)
	    		
	    		if (index_year < year):
	    				year, month = index_year, index_month
    			
    			elif (index_year < year) and (index_month <= month):
    				year, month = index_year, index_month

	    	return year, month

        if (limit == 'new'):
        	year, month = getNewst()
        	print 'The last restaurant was open on the month {0} of {1}' .format(month, year)
    	
    	elif (limit == 'old'):
    		year, month = getOldest()
    		print 'The oldest restaurant was open on the month {0} of {1}' .format(month, year)
        else:
        	print 'wrong arguments on getOldest()'
        	exit(1)
    		   
    	


