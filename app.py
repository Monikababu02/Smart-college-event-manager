import qrcode
import uuid
import mysql.connector

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import os
os.makedirs("static/qrcodes", exist_ok=True)


# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hack')
def input1():
    return render_template('hack.html')

@app.route('/events')
def input5():
    return render_template('events.html')

@app.route('/coding')
def input2():
    return render_template('coding.html')

@app.route('/cyber')
def input3():
    return render_template('cyber.html')

@app.route('/aiml')
def input4():
    return render_template('aiml.html')

@app.route('/signup')
def input7():
    return render_template('signup.html')

@app.route('/login')
def input9():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']  
        phone_no = request.form['phone_no']
        email = request.form['email']

        # Unique registration ID
        registration_id = str(uuid.uuid4())
        event = "Hackathon"

        # Save to database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="benny=2004",
            database="EventManager"
        )
        cursor = conn.cursor()

        query = """INSERT INTO Registrations (id, name, phone_no, email, event, attendance, awards) 
                   VALUES (%s, %s, %s, %s, %s, 'Absent', NULL)"""
        cursor.execute(query, (registration_id, name, phone_no, email, event))
        conn.commit()

        # Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f"{registration_id},{event}"
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # Save QR Code
        image_filename = f"static/qrcodes/{registration_id}.png"
        img.save(image_filename)

        cursor.close()
        conn.close()

        return render_template("success.html", name=name, qr_code=image_filename)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
