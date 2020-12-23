from django.shortcuts import render
from  app1.models import Test

def get_app(request):
    x = Test.objects.all()
    return render(request, 'index.html', locals())
