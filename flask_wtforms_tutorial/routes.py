import datetime
from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import StockForm
from .charts import *


@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():
    
    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Get the form data to query the api
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
                #Generate error message as pass to the page
                err = "ERROR: End date cannot be earlier than Start date."
                chart = None
            else:
                #query the api using the form data
                err = None
                 
                #THIS IS WHERE YOU WILL CALL THE METHODS FROM THE CHARTS.PY FILE AND IMPLEMENT YOUR CODE
            
                results = getAPIData(time_series, symbol)
                
                results.json()

                nestedName = getNestedName(time_series)
                
                date = []
                open_value = []
                high_value = []
                low_value = []
                close_value = []
                volume_value = []
                

                for results, value in results.json()[nestedName].items():
    
                    if(results >= start_date and results <= end_date):
    
                        date.append(results)
                        open_value.append(float(value["1. open"]))
                        high_value.append(float(value["2. high"]))
                        low_value.append(float(value["3. low"]))
                        close_value.append(float(value["4. close"]))
                        volume_value.append(float(value["5. volume"]))
                
                if(chart_type == 1):
                    chart = printLineGraph(symbol, date, open_value, high_value, close_value, low_value)
                else:
                    chart = printBarGraph(symbol, date, open_value, high_value, close_value, low_value)
                
                #This chart variable is what is passed to the stock.html page to render the chart returned from the api

            return render_template("stock.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("stock.html", form=form, template="form-template")
