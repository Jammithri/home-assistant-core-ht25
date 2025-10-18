"""Email notification handler for Google Tasks integration."""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import smtplib

_LOGGER = logging.getLogger(__name__)


def send_email_notification(task_list, email_config):
    """Send a daily reminder email with the given tasklist."""

    msg = MIMEMultipart()
    msg["From"] = email_config["sender_email"]
    msg["To"] = email_config["recipient_email"]
    msg["Subject"] = "Daily Reminder"
    body = "Here is your Google Tasks to-do list for today:\n" + "\n".join(
        f"- {task}" for task in task_list
    )
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_config["sender_email"], email_config["sender_password"])
        server.sendmail(
            email_config["sender_email"],
            email_config["recipient_email"],
            msg.as_string(),
        )
        server.quit()
        _LOGGER.info("Email sent successfully!")
    except Exception:
        _LOGGER.exception("Error: %s Email not sent!!")


# For testing only

# SENDER_EMAIL = "meenu2411as@gmail.com"
# SENDER_PASSWORD = "nchk yflh zmdh ybdz"
# RECIPIENT_EMAIL = "meaa24@student.bth.se"

# if __name__ == "__main__":
#     email_config = {
#         "sender_email": "meenu2411as@gmail.com",
#         "sender_password": "nchk yflh zmdh ybdz",
#         "recipient_email": "meaa24@student.bth.se",
#     }

#     task_list = ["Doctor's appointment at 3pm", "Finish HA integration"]

#     send_email_notification(task_list, email_config)
