import urllib2
import json
import smtplib
import time
	
def sendEmail(newIP):
	fromaddr = ''
	toaddrs  = ''

	# Credentials (if needed)
	username = ''
	password = ''

	msg = str(newIP)+"\n\nThe RasPi IP changed!"

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs ,msg)
	print "Email sent to notify!"
	server.quit()


MINUTES_BETWEEN_CHECKS=60
oldIP = '0.0.0.0' #no need to change to anything
while True:
	response = urllib2.urlopen('http://www.realip.info/api/p/realip.php')
	html = response.read()


	data = json.loads(html)
	currentIP = data['IP']


	if oldIP != currentIP:
		oldIP = currentIP
		print "The IP has changed to", currentIP
		sendEmail(currentIP)
	else:
		print "No IP change"

	time.sleep(MINUTES_BETWEEN_CHECKS*60)
