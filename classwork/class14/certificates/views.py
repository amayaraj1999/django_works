from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from io import BytesIO
from xhtml2pdf import pisa
from django.utils.dateformat import DateFormat

from .forms import CertificateForm
from .models import Certificate

def home(request):
    return render(request, "home.html")

def generate_pdf(context):
    template = get_template("certificate_template.html")
    html = template.render(context)
    result = BytesIO()
    pisa.CreatePDF(html, dest=result)
    return result

def issue_certificate(request):
    if request.method == "POST":
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()

            # Format date as DD/MM/YYYY
            formatted_date = DateFormat(certificate.completion_date).format('d/m/Y')

            context = {
                "student_name": certificate.student_name,
                "course_name": certificate.course_name,
                "completion_date": formatted_date,
            }

            # Generate PDF
            pdf_file = generate_pdf(context)

            # Send Email with PDF
            email = EmailMessage(
                "Your Course Completion Certificate",
                f"Dear {certificate.student_name},\n\n"
                f"Congratulations! You have successfully completed {certificate.course_name} "
                f"on {formatted_date}. Please find your certificate attached.",
                "noreply@class14.com",
                [certificate.student_email],
            )
            email.attach("certificate.pdf", pdf_file.getvalue(), "application/pdf")
            email.send()

            # Return PDF as download
            response = HttpResponse(pdf_file.getvalue(), content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="certificate_{certificate.student_name}.pdf"'
            return response
    else:
        form = CertificateForm()

    return render(request, "issue_certificate.html", {"form": form})
