from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    subject='TEST'
    message="Great it's working"
    from_email="from whicg email we want to send"
    try:
        send_mail(subject, message, from_email, ["To whome we want to send email"])
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    return HttpResponseRedirect("/contact/thanks/")
    