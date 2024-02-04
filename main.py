from flask import Flask, render_template, request, flash, redirect, url_for
from twilio.rest import Client
from flask import Flask, render_template, request, flash, redirect, url_for, session
#from flask import Flask, render_template, request, flash, redirect, url_for, session



# Twilio credentials
account_sid = 'AC6d41d3e8e316951f98fe3dae24140f75'
auth_token = 'f669ae75f71e081038919ad459ea82a6'
twilio_phone_number = '+15128724460'


app = Flask(__name__)
app.secret_key = 'bhgsfdf673j4h3i8y874'  # Replace with your secret 
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')
    
@app.route('/pages')
def pages():
    return render_template('index.html')    
    
@app.route('/rooms')
def rooms():
    return render_template('rooms.html')    

@app.route('/room_details')
def room_details():
    return render_template('room-details.html') 

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog-details')
def blog_details():
    return render_template('blog-details.html')

@app.route('/blog-details1')
def blog_details1():
    return render_template('blog-details1.html')

@app.route('/blog-details2')
def blog_details2():
    return render_template('blog-details2.html')

@app.route('/blog-details3')
def blog_details3():
    return render_template('blog-details3.html')

@app.route('/blog-details4')
def blog_details4():
    return render_template('blog-details4.html')

@app.route('/blog-details5')
def blog_details5():
    return render_template('blog-details5.html')

@app.route('/blog-details6')
def blog_details6():
    return render_template('blog-details6.html')

@app.route('/blog-details7')
def blog_details7():
    return render_template('blog-details7.html')

@app.route('/blog-details8')
def blog_details8():
    return render_template('blog-details8.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    full_name = request.form['full-name']
    email = request.form['email']
    mobile_number = '+91' + request.form['mobileNumber']  # Assuming +91 is the country code
    datetime = request.form['datetime']

    # Create a message for the submitted mobile number
    submitted_message = f"Woohoo! {full_name}, Your visit to Glory Resort on {datetime}, is booked and confirmed! Any queries? Reach out at  (+91) 93000-66044, and for extra details, visit www.glorybyshrida.com. We're eagerly anticipating your visit, See You Soon. Regards Glory Resort."

    # Create a message for the admin
    admin_message = f"Hello Admin, {full_name} has booked a visit on {datetime}. Please contact {mobile_number} or email at {email}."

    # Send Twilio SMS notifications
    client = Client(account_sid, auth_token)

    # Send message to submitted mobile number
    client.messages.create(
        body=submitted_message,
        from_=twilio_phone_number,
        to=mobile_number
    )

    # Send message to admin (e.g., +919993171110)
    admin_phone_number = '+919993171110'
    client.messages.create(
        body=admin_message,
        from_=twilio_phone_number,
        to=admin_phone_number
    )

    # Store a flash message in the session
    session['success_message'] = "Visit booked Successfully!!"

    # Redirect back to the form page with empty values
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
