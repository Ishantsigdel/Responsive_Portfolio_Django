from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def about(request):

    return render(request, 'about.html')

def services(request):

    return render(request, 'services.html')

def testimonial(request):

    return render(request, 'testimonial.html')

def contact(request):
    
    return render (request, 'contact.html')

def footer(request):

    return render(request, 'footer.html')