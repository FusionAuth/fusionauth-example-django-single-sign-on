from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='django_sso_app/authentication.html')
