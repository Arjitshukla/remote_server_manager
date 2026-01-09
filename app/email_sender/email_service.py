import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

def send_email(to_email: str, subject: str, content: str):
    if not SENDGRID_API_KEY:
        raise Exception("SendGrid API key not found")

    message = Mail(
        from_email="your_verified_email@domain.com",
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code, response.body, response.headers
    except Exception as e:
        print("Error sending email:", e)
        return None
