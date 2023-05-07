import json
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for, redirect, flash, make_response, jsonify

app = Flask(__name__)

app.debug = True

@app.route('/parseHTML', methods=['GET'])
def parse_html():
	print("Here?????")
	htmlpage = request.args.get('htmlpage')
	soup = BeautifulSoup(htmlpage,"html.parser")
	title = soup.find("meta", {"property": "og:title"}).get("content")
	print(title)
	description = soup.find("meta", {"property": "og:description"}).get("content")
	url = soup.find("meta", {"property": "og:url"}).get("content")
	typee = soup.find("meta", {"property": "og:type"}).get("content")
	return jsonify({"title":title,"description":description,"url":url,"type":typee})

@app.route('/getjson', methods=['GET'])
def get_json():
	with open('../data/NYT_Politics.json','r', encoding='utf-16') as f:
		data = json.load(f)
	return jsonify(data)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_message='uncaught exception'), 500

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response
  
if __name__ == '__main__':
    app.run(host="0.0.0.0")