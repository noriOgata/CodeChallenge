# CodeChallenge
To run the application:

Open the Terminal and change directory to 'CodeChallenge'

Run the program with ./checkSum.py

Open your preferred web browser and enter the address for authenticate: localhost:5000/authenticate?username='any_name'. This is a faux authenticate so no password is needed. This will create a session that will last for 3 minutes before timing out.

Next go to the address localhost:5000/createchecksum?url='your_url'

The resulting url should show in the browser, copy the address.

Then in the address bar or new tab go to localhost:5000/verifychecksum?url='url_created' this includes the added checksum argument. If the url does not match exactly with the original url it will return a 400 BAD REQUEST and if the checksum differs it will be a bad request.

If you'd like to try again you can use the localhost:5000/logout to exit the current session and start over with a new user.

Every user appends their username to the secret key when the check sum is created so as long as the usernames are unique so is the url and checksum.
