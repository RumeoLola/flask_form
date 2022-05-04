# REPLACE krishjain02939@gmail.com with your email and password 

from flask import Flask
from flask_mail import Mail, Message
from flask import request, redirect
from hawkey import Subject


app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'warutaom.z@gmail.com'
app.config['MAIL_PASSWORD'] = 'P3#k3000'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    meesage = request.form['meesage']
    msg = Message('Get-Quote Form', sender = 'warutaom.z@gmail.com', recipients = ['wasiuomololaz@gmail.com'])
    msg.body = 'Name is: {} \n Email is: {} \n and Subject is: {} \n and the message is {}'.format(name, email, subject, meesage)
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug = True)
