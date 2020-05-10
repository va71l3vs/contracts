from django.shortcuts import render

# Create your views here.
def mycontracts(request):
    return render(request, 'mycontracts/mycontracts.html', {})
