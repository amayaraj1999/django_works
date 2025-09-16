from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.full_name = form.cleaned_data['full_name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.save()
            return render(request, 'thankyou.html', {
                'message': f"Thank you, {form.cleaned_data['full_name']}, for submitting your contact information!"
            })
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
