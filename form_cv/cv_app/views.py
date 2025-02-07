from django.shortcuts import render, redirect
from cv_app.froms import CVForm
from .models import CV
from django.core.mail import send_mail
from django.conf import settings

def create_cv(request):
    if request.method == "POST":
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cv_list')
    else:
        form = CVForm()
    return render(request, 'cv_app/cv_form.html', {'form': form})

def cv_list(request):
    cvs = CV.objects.all()
    return render(request, 'cv_app/cv_list.html', {'cvs': cvs})

def share_cv_email(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    recipient_email = request.POST.get('email')

    if recipient_email:
        subject = f"Резюме {cv.name}"
        message = f"Посмотрите резюме {cv.name} здесь: {request.build_absolute_uri(cv.profile_picture.url)}"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

    return redirect('cv_list')
