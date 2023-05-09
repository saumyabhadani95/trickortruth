import json
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, url_for, redirect, flash, make_response, jsonify
import os
import glob

app = Flask(__name__)

app.debug = True

@app.route('/totgetdata', methods=['GET','POST'])
def get_data():
	urll = request.args.get('url').strip()
	cwd = os.getcwd()
	os.chdir("../data/collection")
	all_files = sorted(glob.glob("*.json"))
	tot_data = 0
	final_rating = 0
	for filee in all_files:
		with open(filee) as fin:
			data = json.loads(fin.read())
			url_data = data['url']
			if url_data == urll:
				tot_data = tot_data + 1
				misleading_rating = data['misleading_rating']
				if misleading_rating == "strong_disagree":
					final_rating = final_rating + 1
				elif misleading_rating == "disagree":
					final_rating = final_rating + 2
				elif misleading_rating == "neutral":
					final_rating = final_rating + 3
				elif misleading_rating == "agree":
					final_rating = final_rating + 4
				else:
					final_rating = final_rating + 5
	os.chdir(cwd)
	if tot_data < 4:
		return "NA"
	else:
		final_rating = final_rating/tot_data
		print(final_rating)
		if final_rating == 3.0:
			return "NA"
		elif final_rating < 2.0:
			return "Very Misleading"
		elif final_rating < 3.0:
			return "Leans Misleading"
		elif final_rating < 4.0:
			return "Leans Accurate"
		else:
			return "Very Accurate"
	return "Done!"

@app.route('/totstoredata', methods=['GET','POST'])
def store_data():
	print("Here!!!")
	cwd = os.getcwd()
	urll = request.args.get('url')
	misleading_rating = request.args.get('misleading_rating')
	biased_rating = request.args.get('biased_rating')
	clarity_rating = request.args.get('clarity_rating')
	os.chdir("../data/collection")
	all_files = sorted(glob.glob("*.json"))
	new_file_number = 1
	if all_files:
		latest_file = max(all_files, key=lambda fn: int(fn.split(".")[0]))
		new_file_number = int(latest_file.split(".")[0]) + 1
	with open(str(new_file_number)+".json","w") as fout:
		fout.write(json.dumps({"url":urll,"misleading_rating":misleading_rating,"biased_rating":biased_rating,"clarity_rating":clarity_rating}))
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
    app.run(host="0.0.0.0",port=6001)