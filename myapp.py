# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:21:03 2018

@author: prajit kk
"""

from flask import Flask,render_template,request
app = Flask(__name__)

alphabets1 = "qwertyuiopzx"
alphabets2 = "asdfghjklmnbcv"

live1 = "you are going to live"
live2 = "you seem like a noble leader it's time to join avengers"
die1 = "hope they remember you"
die2 = "smile and Be thankful, that your meaningless lives are now contributing to the universe"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    first_name = request.args.get("name")
    print(first_name[0])
    if first_name[0] in alphabets1:
        return render_template("result.html", line1 = die1, line2 = die2)
    else:
        return render_template("result.html", line1 = live1 , line2 = live2 )


if __name__ == '__main__':
   app.run()