from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_email(subject, body, recipient_list, button_url=None, button_text=None):
    html_content = render_to_string("base_email_template.html", {
        "subject": subject,
        "body": body,
        "button_url": button_url,
        "button_text": button_text,
    })

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body, 
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
