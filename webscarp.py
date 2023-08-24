from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/scrape": {"origins": "https://chat.openai.com"}})  # Enable CORS for the '/scrape' endpoint

@app.route('/scrape', methods=['GET','POST'])
def scrape():
    url = request.json.get('url')
    print(f'Received URL: {url}')  # Add this line to print the received URL
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        main_text = soup.get_text()
        print(f'Sending response: {main_text[:50]}...')  # Add this line to print a snippet of the response being sent
        return jsonify({'main_text': main_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
