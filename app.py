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
	info = compareToLast(sample['firstName'], sample["lastName"], sample["Glucose"], sample["Insulin"], sample["CarbIntake"])
	return render_template('newPage.html', info=info)
	#return redirect(url_for('main'))

@app.route('/results')
def returnResults():
	return jsonify(databaseFile)

def compareToLast(firstName, lastName, glucose, insulin, carbIntake):
	try:
		with open('database.json') as json_data:
		    databaseFile = json.load(json_data)
	except Exception as exp:
		print exp
		databaseFile = []
	glevel = glucose
	ilevel = insulin
	clevel = carbIntake
	print databaseFile
	try:
		allGVals = []
		allCVals = []
		allIVals = []
		for var in databaseFile:
			if var['firstName'] == firstName and var['lastName'] == lastName:
				allGVals.append(int(var['Glucose']))
				allCVals.append(int(var["CarbIntake"]))
				allIVals.append(int(var['Insulin']))
		if len(allGVals) == 1:
			glucose = False
			carbIntake = False
			insulin = False
		else:
			glucose = ((float(sum(allGVals)) / float(len(allGVals))) > glucose)
			carbIntake = ((float(sum(allCVals)) / float(len(allCVals))) > carbIntake)
			insulin = ((float(sum(allIVals)) / float(len(allIVals))) > insulin)
	except Exception as exp:
		print(exp)
		glucose = False
		carbIntake = False
		insulin = False
	if glucose == True:
		glucose = "Higher"
	else:
		glucose = "Lower"
	if carbIntake == True:
		carbIntake = "Higher"
	else:
		carbIntake = "Lower"
	if insulin == True:
		insulin = "Higher"
	else:
		insulin = "Lower"
	return {"Glucose": {"Level": glevel, "High": glucose}, "carbIntake": {"Level": clevel, "High": carbIntake}, "Insulin": {"Level": ilevel, "High": insulin}}


if __name__ == "__main__":
	app.run(host='0.0.0.0')
