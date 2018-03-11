import sys
reload(sys)
sys.setdefaultencoding('UTF8')
from flask import Flask, request, jsonify, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response
import json

app = Flask(__name__,template_folder="templates/",static_url_path='/static')
try:
	with open('database.json') as json_data:
	    databaseFile = json.load(json_data)
except:
	databaseFile = []

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/submitForm', methods=["POST"])
def addData():
	sample = request.form.to_dict()
	databaseFile.append(sample)
	with open('database.json', 'w') as fp:
		json.dump(databaseFile, fp)
	#return render_template('newPage.html')
	return redirect(url_for('main'))


if __name__ == "__main__":
	app.run()
