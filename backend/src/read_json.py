import json
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for, redirect, flash, make_response, jsonify
import os
import glob

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

@app.route('/storedata', methods=['GET','POST'])
def store_data():
	cwd = os.getcwd()
	urll = request.args.get('url')
	misleading_rating = request.args.get('misleading_rating')
	biased_rating = request.args.get('biased_rating')
	clarity_rating = request.args.get('clarity_rating')
	os.chdir("../data/collection/")
	all_files = sorted(glob.glob("*.json.gz"))
	new_file_number = 1
	if all_files:
		latest_file = max(all_files, key=lambda fn: int(fn.split(".")[0]))
		new_file_number = int(latest_file.split(".")[0]) + 1
	with open(str(new_file_number)+".json","w") as fout:
		fout.write(json.dumps({"url":url,"misleading_rating":misleading_rating,"biased_rating":biased_rating,"clarity_rating":clarity_rating}))
	os.chdir(cwd)
	return "Done!"

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
    app.run(host="0.0.0.0",port=6000)