#Import Pre-requesites
from flask import Flask, jsonify, render_template, request
import requests
import pymysql

#Connect to sql db function
def connectsql():
    #set the con variable (host, user, password, db)
    con = pymysql.connect(host="localhost", user="testflask", passwd="", db="testflask")
    #set cur as cursor
    cur = con.cursor()
    #return the variables
    return cur, con

#Define the app
app = Flask(__name__, static_url_path='')

#Define route similar to localhost/names
@app.route("/names")
# Make games function
def games():
    # Define cursor and connection from sql connect function
    cur, con = connectsql()
    #Run SQL Commands
    cur.execute("SELECT * FROM Names")
    #Set data with return from db
    data = cur.fetchall()
    #Close connections
    cur.close()
    con.close()
    #Render the page
    return render_template("results.html", api_data=data)

#Run the program
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=83, debug=True)
