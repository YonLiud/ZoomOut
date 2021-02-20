from flask import Flask,redirect,url_for,render_template,request
import time


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    isActive = False
    if request.method=='POST':
        endtime = request.form["endtime"]
        isActive = True
        return render_template('index.html', endtime=endtime, isActive=isActive)
    return render_template('index.html')

@app.route('/close', methods=["GET"])
def close():
    return "closed"
    

if __name__ == '__main__':
    app.run(port=5000,debug=True)