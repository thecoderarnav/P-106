import csv
import plotly.express as  px 
import numpy as np 

def getdatasource(data_path):
    marksinpercentage = []
    dayspresent = []
    
    with open ("data2.csv")  as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
             marksinpercentage.append(float(row ["Marks In Percentage"]))
             dayspresent.append(float(row ["Days Present"]))

    return{"x":dayspresent,"y": marksinpercentage}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation in between the Marks and Days is ", correlation[0,1])        

def setup():
    data_path = "./data2.csv"
    datasource = getdatasource(data_path)
    findcorrelation(datasource)

setup()    
