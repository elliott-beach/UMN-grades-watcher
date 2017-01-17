#!/usr/bin/env python

import mechanize
import threading
import smtplib
import email

LOGIN = 'https://ay16.moodle.umn.edu/login'
GRADES = 'https://ay16.moodle.umn.edu/grade/report/user/index.php'
EMAIL_DOMAIN = '@umn.edu'

# source: http://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def get_grades(username, password, courseID):
	"""get all grades for a student with an individual courseID"""
	browser = mechanize.Browser()
	browser.open(LOGIN)
	browser.select_form(nr=1)
	browser.form['j_username'] =  username
	browser.form['j_password'] =  password
	browser.submit()
	# Hop through the page: "JavaScript is disabled, so you must click the submit button".
	browser.select_form(nr=0)
	browser.submit()
	response = browser.open(GRADES + '?id=' + courseID)
	return response.read()

def send_email(me, you, subject, body):
	# me == the sender's email address
	# you == the recipient's email address
	message = email.mime.text.MIMEText(body)
	message['Subject'] = subject
	message['From'] = me
	message['To'] = you
	# Send the message via our own SMTP server, but don't include the
	# envelope header.	
	s = smtplib.SMTP('localhost')
	s.sendmail(me, [you], msg.as_string())
	s.quit()

class GradesWatcher():

	def __init__ (self, username, password, courseID):
		self.username = username
		self.password = password
		self.courseID = courseID
		
	def check_grades(self):
		updated_grades = get_grades(self.username, self.password, self.courseID)
		if updated_grades != self.grades:
			self.notify_grade_change()
		self.grades = updated_grades

	def notify_grade_change(self):
		email_address = username + EMAIL_DOMAIN
		send_email('beach144@umn.edu', email_address, 'Grades Changed', GRADES)
		# send an email to the email address that grades have changed

	def run(self):
		# Check for changes grades every hour.
		self.grades = get_grades(self.username, self.password, self.courseID)
		set_interval(self.check_grades, 60 * 60 )

HELP = """
usage: ./mech.py <name> <password> <courseID> <courseID> ...
"""

if __name__ == "__main__":
	from sys import argv
	argv.pop(0) # discard the script name
	name = argv[0]
	pwd = argv[1]
	courseIDs = argv[2:]
	for ID in courseIDs:
		GradesWatcher(name, pwd, ID).run()
	print "Watching your grades!"






