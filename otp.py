import smtplib
from email.mime.text import MIMEText
import pyotp


def generate_otp():
    totp = pyotp.TOTP('base32secret3232')
    return totp.now()


def send_otp_via_email(receiver_email, otp):
    # Email settings
    sender_email = "your-email@example.com"
    password = "your-email-password"

    # Create the email
    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = 'OTP for your transaction'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    # Use your actual SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
