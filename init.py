#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import hashlib
from stats.StatsCollector import statsResponseState, statsResponseCounty, statsResponseCountry
import sys


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
    if 'email' in session:
        return redirect(url_for('home'))
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
    country = request.form['country']
    state = request.form['state']
    query = "SELECT * FROM Person WHERE email = %s"
    cursor = conn.cursor()
    cursor.execute(query,(email))
    data = cursor.fetchone()
    print("HELLLOOOOOO " + state, flush = True)
    if data == None:
        if state == "Definition":
            state = None
        ins = "INSERT INTO Person VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(ins, (email, password, firstName, lastName, phoneNumber,country,state))
        conn.commit()
        cursor.close()
    return render_template("index.html")

@app.route('/home',methods=['GET','POST'])
def home():
    if 'email' in session:
        query = "SELECT country, state FROM Person where email = %s"
        cursor = conn.cursor()
        cursor.execute(query,(session['email']))
        data = cursor.fetchone()
        countryStat = statsResponseCountry(data['country'])
        print(countryStat, flush=True)
        stateStat = None
        if data['state'] and data['country'] == "USA":
            stateStat = statsResponseState(data['state'])
            print(stateStat, flush=True)
        return render_template('home.html',email = session['email'], countryStats = countryStat, stateStats = stateStat)
    return redirect(url_for('hello'))

@app.route('/account',methods = ['GET','POST'])
def account():
    return render_template('account.html')
@app.route('/statistics', methods =['GET','POST'])
def statistics():
    if 'email' in session:
        return render_template('/statistics.html')
    return render_template('index.html')

@app.route('/request', methods =['GET','POST'])
def requests():
    if 'email' in session:
        return render_template('/request.html')
    return render_template('index.html')

@app.route('/contact', methods =['GET','POST'])
def contact():
    return render_template('/contact.html')

@app.route('/about', methods =['GET','POST'])
def about():
    return render_template('/about.html')

@app.route('/logout', methods = ['GET','POST'])
def logout():
    if session['email']:
        session.pop('email')
    return redirect(url_for('hello'))

app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
