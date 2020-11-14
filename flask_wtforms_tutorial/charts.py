'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import pygal as py


#Helper function for converting date
def convert_date(str_date):
    tmpDate = datetime.strptime(str_date, '%Y-%m-%d').date()
    return tmpDate.strftime('%Y-%m-%d')

def getAPIData(userChoices, symbol):

    if(userChoices == "1"):
        payload = {'function':'TIME_SERIES_INTRADAY','symbol':symbol,'interval':'30min','apikey':'P8HT9FLVF2HF2HZB'}
    elif(userChoices == "2"):
        payload = {'function':'TIME_SERIES_DAILY','symbol':symbol,'apikey':'P8HT9FLVF2HF2HZB'}
    elif(userChoices == "3"):
        payload = {'function':'TIME_SERIES_WEEKLY','symbol':symbol,'apikey':'P8HT9FLVF2HF2HZB'}
    else:
        payload = {'function':'TIME_SERIES_MONTHLY','symbol':symbol,'apikey':'P8HT9FLVF2HF2HZB'}

    results = requests.get('https://www.alphavantage.co/query', params=payload)
    
    
    return results
    
def getNestedName(userChoices):

    if(userChoices == "1"):
        nestedName = "Time Series (30min)"
    elif(userChoices == "2"):
        nestedName = "Time Series (Daily)"
    elif(userChoices == "3"):
        nestedName = "Time Series (Weekly)"
    else:
        nestedName = "Time Series (Monthly)"
    
    return nestedName
    
def printLineGraph(symbol,dates, open_value, high_value, close_value, low_value):

    line = py.Line(x_label_rotation=20, width=2000)
    line.title = symbol  # Set the title of the line chart
    line.x_labels = dates  # Setting the labels for x-axis
    line.add('Open Values', open_value)  #setting data
    line.add('High Values', high_value)
    line.add('Close Values', close_value)
    line.add('Low Values', low_value)
    
    graphData = line.render_data_uri()
    return graphData


def printBarGraph(symbol, dates, open_value, high_value, close_value, low_value):

    line_chart = py.Bar(width=2000, x_label_rotation=20)
    line_chart.title = symbol
    line_chart.x_labels = dates
    line_chart.add('Open Values', open_value)  # setting data
    line_chart.add('High Values', high_value)
    line_chart.add('Close Values', close_value)
    line_chart.add('Low Values', low_value)
    
    graphData = line_chart.render_data_uri()
    return graphData