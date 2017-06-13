from django.shortcuts import render
# from django.core.mail import send_mail
# Create your views here.
from .emails import send_contact_message, send_simple_message


def view_resume(request):

    request_status = 0
    con_name = "buddy"

    if request.method == "POST":
        con_name = request.POST.get("name", "")
        con_email = request.POST.get("email", "")
        con_subject = request.POST.get("subject", "")
        con_message = request.POST.get("message", "")

        # mail_request = send_simple_message()      # Testing
        mail_request = send_contact_message(con_name, con_email, con_subject, con_message)
        request_status = mail_request.status_code
        print(con_name, mail_request.status_code)

        return render(request, 'resume.html', {'status_code': request_status, 'con_name': con_name})
    return render(request, 'resume.html', {'status_code': request_status, 'con_name': con_name})
