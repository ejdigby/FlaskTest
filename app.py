from flask import Flask, jsonify, render_template, request
import requests
import pymysql

def connectsql():
    con = pymysql.connect(host="localhost", user="testflask", passwd="", db="testflask")
    cur = con.cursor()
    return cur, con


app = Flask(__name__, static_url_path='')

@app.route("/names")
def games():

    print "running function again"
    cur, con = connectsql()
    cur.execute("SELECT * FROM Names")
    data = cur.fetchall()
    cur.close()
    con.close()
    return render_template("results.html", api_data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=83, debug=True)
