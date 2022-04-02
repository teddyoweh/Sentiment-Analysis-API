# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddyoweh@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Questions.
from flask import url_for, redirect, render_template, flash, g, session

from flask import jsonify
from app import main
import app.models 
from app.models import analyzeSentiment

from flask import request
from textblob import TextBlob






@main.route('/', methods=['GET'])
def index():
    text = request.args.get('text')
    if text!=None:
    
    
        out=analyzeSentiment.result(text)
        
        output = {
            'Text': out[0],
            'Sentiment':out[1],
            'Sentiment Level':out[2],
            'Polarity':out[3],
            'Subjectivity':out[4]
            
            
        }
        print(output)
        return jsonify(output)

    else:
        return '<span style="font-family:monospace;">No Arguments provided</span> <a  href="./?text=Im a developer">Sample</a>'














"""

class example:
    def __init__(self) -> None:
        pass
    def returnlist(variable1)->list:
        list1 = [variable1,'codes']
        return list1
    def returndict(variable1)->dict:
        variable1 = str(variable1).capitalize()
        dict1 = {
			'name'     :'teddyoweh',
  			'title'    : f'{variable1} Developer',
  			'email'    : 'teddy@teddyoweh.com',
			 
  
		}
        return dict1
 
@app.route('/')
def index():
	return render_template('index.html')


 
@app.route('/')
def index():
	 
    d =example.returnlist('teddy')
    return jsonify(d)

@app.route('/view', methods=['GET'])
def arg():
    lang = request.args.get('lang')
    b =example.returndict(lang)
    return jsonify(b)
"""
# ====================
