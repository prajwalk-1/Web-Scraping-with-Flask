import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def fetch_data(page_num, count):
    url = f"https://archive.org/services/offshoot/home-page/collections.php?page={page_num}&count={count}"
    response = requests.get(url)

    if response.status_code == 200:
        # Convert the JSON response to a Pandas DataFrame
        data = pd.DataFrame(response.json()["value"]["docs"])
        return data[['identifier', 'title', 'item_count']]
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        page_start = request.form.get('page_start')
        page_end = request.form.get('page_end')
        count = request.form.get('count')

        # Check if any of the required fields are missing
        if not page_start or not page_end or not count:
            return "Please provide all required fields."
        try:
            page_start = int(page_start)
            page_end = int(page_end)
            count = int(count)
        except ValueError:
            return "Invalid input. Please enter valid numbers."

        all_data = pd.DataFrame(columns=['identifier', 'title', 'item_count'])

        # Fetch data from archive.org for each page in the range
        for page_num in range(page_start, page_end + 1):
            data = fetch_data(page_num, count)
            if data is not None:
                all_data = all_data.append(data, ignore_index=True)

        if not all_data.empty:
            # Render the HTML table using Pandas DataFrame
            table_html = all_data.to_html(classes='table table-striped', index=False)
            return render_template('index1.html', table=table_html)
        else:
            return "Error fetching data from archive.org"

    return render_template('index1.html', table=None)

if __name__ == '__main__':
    app.run(debug=True)

