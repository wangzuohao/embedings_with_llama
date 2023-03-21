# Import necessary packages
from flask import Flask, render_template, request
from llama_index import GPTSimpleVectorIndex
import os

app = Flask(__name__)

# Please setup the env for OpenAI API key with the following command in Linux
# export OPENAI_API_KEY='sk-xxxxxxxxx'

# Load the index from index.json
index1 = GPTSimpleVectorIndex.load_from_disk('./index.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    response = index1.query(query)
    if response:
        if isinstance(response, list):
            response = '\n'.join(response)
        return render_template('index.html', query=query, response=response)
    else:
        return render_template('index.html', query=query, response='No information found.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
