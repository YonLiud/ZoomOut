from flask import Flask,redirect,url_for,render_template,request
import time
import os
import converter
import threading

app=Flask(__name__)
stop = False

def timer(endtime):
    endtime = endtime*60
    print(endtime)
    while endtime:
        if not stop:
            mins, secs = divmod(endtime, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            endtime -= 1
        else:
            break
    os.system('taskkill /F /IM "zoom.exe"')



@app.route('/',methods=['GET','POST'])
def home():
    isActive = False
    if request.method=='POST':
        endtime = request.form["endtime"]
        print(endtime)
        isActive = True
        deltatime = converter.deltaTime(endtime)
        x = threading.Thread(target=timer, args=(deltatime,))
        x.start()
        return render_template('index.html', endtime=endtime, isActive=isActive, deltatime=deltatime)
    return render_template('index.html')

@app.route('/close', methods=["GET"])
def close():
    stop = True
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    os.system("echo [91mClosing App[0m")
    return "<h1>ZoomOut has been closed</h1>"



if __name__ == '__main__':
    app.run(port=5000,debug=True)