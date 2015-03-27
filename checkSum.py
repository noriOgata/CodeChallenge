#!flask/bin/python
from flask import Flask, jsonify, abort, request
import hashlib, urllib

app = Flask(__name__)
app.secret_key = 'S6I5sAR7JHWqQQ=='
@app.route('/createchecksum')
def createCheckSum():
	if request.args.has_key('url') == False:
		abort(404)
	mainUrl = request.args.get('url')
	
	for key, val in request.args.iteritems():
		if key != 'url':
			s = ""
			s += str(key) + '=' + str(val)
			mainUrl += '&' + s
	
	checkSum = hashlib.md5(app.secret_key).hexdigest()	
	returnUrl = mainUrl + "&checksum=" + checkSum
	return returnUrl 

@app.route('/verifychecksum')
def verifyCheckSum():
	if request.args.has_key('url') == False:
		abort(404)
	elif request.args.has_key('checksum') == False:
		abort(400)

	localCheckSum = hashlib.md5(secretKey).hexdigest()
	if localCheckSum != request.args.get('checksum'):
		abort(400)	
	
	return "checksum Verified!"

if __name__ == '__main__':
	app.run(host='0.0.0.0')
