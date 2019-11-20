from flask import Flask, render_template, request
from pytrends.request import TrendReq
import csv
import pandas as pd
import numpy

app = Flask("App")

@app.route("/")
def hello():
	pytrend = TrendReq(hl='en-UK' , tz=0)
	kw_list=['Last Cristmas']

	# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
	#pytrend.build_payload(kw_list=['Last Cristmas'],geo='GB-SCT',gprop='youtube',timeframe='today 1-d')
	pytrend.build_payload(kw_list=['Last Christmas','Jingle Bells'],geo='GB',gprop='youtube',timeframe='now 1-H')
	interest_over_time_df = pytrend.interest_over_time()
	print(interest_over_time_df.head())

	names = ['x','y','z']
	interest_over_time_df.columns = names
	print(interest_over_time_df.head())

	nLC=interest_over_time_df[['x','y']].sum()[0]
	nJB=interest_over_time_df[['x','y']].sum()[1]


	print(nLC)
	print(nJB)
	return render_template("projecthtml.html", nLC=nLC, nJB=nJB)

@app.route("/<name>")
def hello_someone(name):
		return render_template("hello.html", name=name.title())

app.run(debug=True)