from flask import Flask,render_template,request
import sys, os
app = Flask(__name__)
@app.route('/date',methods=['GET','POST'])
def formval():
	if request.method=='POST':
		dateval = request.form['datepick']
		return render_template('layout.html',subdate=dateval)
@app.route('/', methods=['GET','POST'])
def value():
	y= u'r718'
	return render_template('layout.html',y=y)
@app.route('/radio', methods=['GET','POST'])
def rad():
		x= 'roger'
		return render_template('layout.html',roger=x)
	
if __name__== '__main__':
	port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
