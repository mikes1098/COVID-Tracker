#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import hashlib

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       port=8889,
                       user='root',
                       password='root',
                       db='COVID-Tracker',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/loginAuth',methods=['GET', 'POST'])
def loginAuth():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM Person WHERE email = %s and password = %s"
    cursor = conn.cursor()
    cursor.execute(query,(email,password))
    data = cursor.fetchone()
    errorM = None
    if data:
        session['email'] = email
        session['firstName'] = data['firstName']
        return redirect(url_for('home'))
    else:
        errorM = "Email and Password combination does not exist. Please try again."
        return render_template("index.html",error = errorM)
    
@app.route('/registerAuth',methods=['GET','POST'])
def registerAuth():
    email = request.form['email']
    password = request.form['password']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    phoneNumber = request.form['phoneNumber']
    query = "SELECT * FROM Person WHERE email = %s"
    cursor = conn.cursor()
    cursor.execute(query,(email))
    data = cursor.fetchone()
    if data == None:
        ins = "INSERT INTO Person VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(ins, (email, password, firstName, lastName, phoneNumber))
        conn.commit()
        cursor.close()
    return render_template("index.html")

@app.route('/home')
def home():
    emailU = session['email']
    return render_template('home.html',email = emailU)



app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
