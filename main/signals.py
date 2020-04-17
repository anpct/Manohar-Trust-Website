from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Event, Email
from django.core.mail import send_mass_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save, sender=Event)
def my_function_post_save(sender, instance, **kwargs):
    html_message = render_to_string('main/mail_template.html', {'instance': instance})
    plain_message = strip_tags(html_message)
    e = Email.objects.all()
    emails = []
    for i in e:
        emails.append(i.email)
    u_emails = []
    for i in emails:
        if i not in u_emails:
            u_emails.append(i)

    send_mass_html_mail('NEW EVENT ANNOUNCEMENT!!', plain_message, html_message,settings.EMAIL_HOST_USER, u_emails)

from django.core.mail import get_connection, EmailMultiAlternatives

def send_mass_html_mail(subject, message, html_message, from_email, recipient_list):
    emails = []
    for recipient in recipient_list:
        email = EmailMultiAlternatives(subject, message, from_email, [recipient])
        email.attach_alternative(html_message, 'text/html')
        emails.append(email)
    return get_connection().send_messages(emails)