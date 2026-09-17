import imaplib
import email
from email.header import decode_header


def fetch_emails(email_address, app_password):

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, app_password)

    mail.select("INBOX")

    status, messages = mail.search(None, "UNSEEN")

    email_list = []

    for num in messages[0].split():
        status, data = mail.fetch(num, "(RFC822)")

        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        sender = msg.get("From")
        subject = msg.get("Subject")

        if subject:
            decoded_subject, encoding = decode_header(subject)[0]

            if isinstance(decoded_subject, bytes):
                subject = decoded_subject.decode(
                    encoding or "utf-8",
                    errors="ignore"
                )

        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)

                    if payload:
                        body = payload.decode(
                            errors="ignore"
                        )
                    break
        else:
            payload = msg.get_payload(decode=True)

            if payload:
                body = payload.decode(
                    errors="ignore"
                )

        email_list.append({
            "sender": sender,
            "subject": subject,
            "body": body
        })

    mail.logout()

    return email_list


    
