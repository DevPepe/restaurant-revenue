from data import Data
from distribution import Distribution

if __name__ == "__main__":
    d = Data("/Users/Navarro/Documents/Kaggle_Competition/Restaurant_Revenue_Prediction/restaurant-revenue/Data/train.csv")
    l = d.getP(37)
    print len(l)