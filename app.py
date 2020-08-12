## Importing Packages ##
from flask import Flask, render_template, request
import pandas as pd
from main import predict

## Initialising the app ##
app = Flask(__name__)
data = {}

@app.route('/')
def student():
   """
   Render the Index.html file
   """
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   """
   Function for returning the result obatined from main.py
   """
   if request.method == 'POST': 
      result = request.form
      ## Converting the input data to a dictionary ##
      for key, value in result.items():
        data.update({key:[value]})
      ## Converting dictionary to a dataframe ##
      df = pd.DataFrame.from_dict(data)
      df.insert(0,"id", 419)
      ## Declaring a variable for the output received from the predict function ##
      predicted = predict(df)
      ## Render the Result.htmml file ##
      return render_template("result.html",result = predicted)

if __name__ == '__main__':
   app.run(debug = True)