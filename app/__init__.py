# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddyoweh@teddyoweh.com
# Message: Feel Free To Contact Me on Enquires or Questions.
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager

main= Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
 

from app import views, models
