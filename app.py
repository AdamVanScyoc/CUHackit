import sys
reload(sys)
sys.setdefaultencoding('UTF8')
from flask import Flask, request, jsonify, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response
import json

app = Flask(__name__,template_folder="templates/",static_url_path='/static')


@app.route('/')
def main():
	return render_template('index.html')

@app.route('/submitForm', methods=["POST"])
def addData():
	try:
		with open('database.json') as json_data:
		    databaseFile = json.load(json_data)
	except:
		databaseFile = []
	sample = request.form.to_dict()
	databaseFile.append(sample)
	with open('database.json', 'w') as fp:
		json.dump(databaseFile, fp)
	info = compareToLast(sample['firstName'], sample["lastName"], sample["Glucose"], sample["Insulin"], sample["carbIntake"])
	return render_template('newPage.html')
	#return redirect(url_for('main'))

@app.route('/results')
def returnResults():
	return jsonify(databaseFile)

def compareToLast(firstName, lastName, glucose, insulin, carbIntake):
	try:
		allGVals = []
		allCVals = []
		allIVals = []
		for var in databaseFile:
			if var['firstName'] == firstName && var['lastName'] == lastName:
				allGVals.append(var['Glucose'])
				allCVals.append(var["CarbIntake"])
				allIVals.append(var['Insulin'])
		if len(allGVals) == 1:
			glucose = False
			carbIntake = False
			insulin = False
		else:
			glucose = (float(sum(allGVals)) / float(len(allGVals)) > glucose)
			carbIntake = (float(sum(allCVals)) / float(len(allCVals)) > carbIntake)
			insulin = (float(sum(allIVals)) / float(len(allIVals)) > insluin)
		except:
			glucose = False
			carbIntake = False
			insulin = False
	return {"Glucose": glucose, "carbIntake": carbIntake, "Insulin": insulin}


if __name__ == "__main__":
	app.run(host='0.0.0.0')
