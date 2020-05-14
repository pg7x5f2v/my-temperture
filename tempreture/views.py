from django.shortcuts import render

def temp_list(request):
    return render(request, 'tempreture/temp_list.html', {})