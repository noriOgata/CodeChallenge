#!flask/bin/python
from datetime import timedelta
from flask import Flask, session, escape, abort, request
import hashlib, urllib

def createUrlWithArgs(main, items):
	for key, val in items:
             if key != 'url' and key != 'checksum':
                 s = ""
                 s += str(key) + '=' + str(val)
                 main += '&' + s
	return main
 

app = Flask(__name__)
app.secret_key = 'S6I5sAR7JHWqQQ=='
app.permanent_session_lifetime = timedelta(minutes=3)

@app.route('/authenticate')
def authenticate():
	if request.args.has_key('username') == False:
		abort(400)
	elif 'name' in session:
		return 'Already logged in as %s' % escape(session['name'])
	
	session.permanent = True
	session['name'] = request.args.get('username')
	return 'Authentification Successful!'

@app.route('/logout')
def logout():
	session.pop('fullUrl', None)
	session.pop('checkSum', None)
	session.pop('name', None)

	return 'Logged out successfully'

@app.route('/createchecksum')
def createCheckSum():
	if request.args.has_key('url') == False:
		abort(404)
	elif 'name' not in session:
		return 'You have not been authenticated'
	
	mainUrl = createUrlWithArgs(request.args.get('url'), request.args.iteritems())	
	
	checkSum = hashlib.md5(app.secret_key + session['name']).hexdigest()	
	returnUrl = mainUrl + "&checksum=" + checkSum
	session['fullUrl'] = mainUrl
	session['checkSum'] = checkSum
	return returnUrl 

@app.route('/verifychecksum')
def verifyCheckSum():
	if request.args.has_key('url') == False:
		abort(404)
	elif request.args.has_key('checksum') == False:
		abort(400)
	elif 'name' not in session:
		return 'You have not been Authenticated'
	
	urlPath = createUrlWithArgs(request.args.get('url'), request.args.iteritems())

	if session['checkSum'] != request.args.get('checksum') or session['fullUrl'] != urlPath:
		session.pop('fullUrl', None)
		session.pop('checkSum', None)
		session.pop('name', None)
		abort(400)	
	
	return "checksum Verified!"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
