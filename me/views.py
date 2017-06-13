from django.shortcuts import render
# from django.core.mail import send_mail
# Create your views here.


def view_resume(request):
    if request.method == "POST":
        con_name = request.POST.get("name", "")
        con_email = request.POST.get("email", "")
        con_subject = request.POST.get("subject", "")
        con_message = request.POST.get("message", "")

        return render(request, 'resume.html', {})
    return render(request, 'resume.html', {})
