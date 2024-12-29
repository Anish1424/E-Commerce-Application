from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
app.static_folder = 'static'

# Read the two datasets into pandas DataFrames
dataset1 = pd.read_csv('AmazonElectronics.csv')
dataset2 = pd.read_csv('FlipkartElectronics.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_query']
    
    # Search in dataset1
    results1 = dataset1[dataset1['name'].str.contains(query, case=False)]
    results_list1 = results1.to_dict(orient='records')

    # Search in dataset2
    results2 = dataset2[dataset2['name'].str.contains(query, case=False)]
    results_list2 = results2.to_dict(orient='records')

    return render_template('results.html', results1=results_list1, results2=results_list2)

if __name__ == '__main__':
    app.run(debug=True) 