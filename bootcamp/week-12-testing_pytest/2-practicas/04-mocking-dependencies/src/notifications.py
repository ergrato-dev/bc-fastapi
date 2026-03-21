"""
Notification service with external dependencies.
"""

import smtplib
from email.mime.text import MIMEText
from dataclasses import dataclass


@dataclass
class EmailConfig:
    """Email configuration."""
    smtp_host: str
    smtp_port: int
    username: str
    password: str


class EmailSender:
    """Real email sender using SMTP."""
    
    def __init__(self, config: EmailConfig):
        self.config = config
    
    def send(self, to: str, subject: str, body: str) -> bool:
        """
        Send an email via SMTP.
        
        In tests, this should be mocked to avoid sending real emails.
        """
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["To"] = to
        msg["From"] = self.config.username
        
        try:
            with smtplib.SMTP(self.config.smtp_host, self.config.smtp_port) as server:
                server.starttls()
                server.login(self.config.username, self.config.password)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False


class NotificationService:
    """Service for sending notifications."""
    
    def __init__(self, email_sender: EmailSender):
        self.email_sender = email_sender
        self._sent_notifications = []
    
    def notify_user(self, user_email: str, message: str) -> bool:
        """Send notification to user."""
        result = self.email_sender.send(
            to=user_email,
            subject="Notification",
            body=message
        )
        
        if result:
            self._sent_notifications.append({
                "email": user_email,
                "message": message,
            })
        
        return result
    
    def notify_multiple(self, emails: list[str], message: str) -> dict:
        """Send notification to multiple users."""
        results = {
            "success": [],
            "failed": [],
        }
        
        for email in emails:
            if self.notify_user(email, message):
                results["success"].append(email)
            else:
                results["failed"].append(email)
        
        return results
    
    def get_sent_count(self) -> int:
        """Get number of sent notifications."""
        return len(self._sent_notifications)
