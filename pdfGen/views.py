from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import io
from .models import Profile
import pdfkit


# Create your views here.

def accept_data(request):

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')
    
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()

    return render(request, 'pdfGen/user-form.html')


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdfGen/list.html', {'profiles': profiles})


def view_resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, 'pdfGen/resume.html', {'user_profile':user_profile})


def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    config = pdfkit.configuration(wkhtmltopdf = r'C:\wkhtmltox\bin\wkhtmltopdf.exe')

    # Load the html template
    template = get_template('pdfGen/resume.html')
    html = template.render({'user_profile':user_profile})

    # Generate pdf using PDFKit
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(html, False, options, configuration=config)

    # Create an HTTP response with the PDF attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response

