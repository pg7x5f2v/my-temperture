from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Temp
from .forms import TempForm
from django.shortcuts import redirect
##from matplotlib import pyplot as plt
import numpy as np
from django.http import HttpResponse
import io
import sqlalchemy
import pandas as pd

'''def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s
    
def img_plot(request):
    # matplotを使って作図する
    engine = sqlalchemy.create_engine("sqlite:///db.sqlite3")
    temp_data = pd.read_sql('SELECT * FROM tempreture_temp WHERE created_date < datetime("now","localtime") AND created_date > datetime("now","localtime", "-30 days")',engine)
    x=temp_data["created_date"]
    y=temp_data["temperture"]
    plt.plot(x,y,marker="o")
    plt.xticks(rotation=90)
    plt.xlabel('x-axis label') 
    plt.subplots_adjust(left=0.1, right=0.95, bottom=0.5, top=0.95)
    ax = plt.subplot()
    ax.scatter(x, y)
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response
'''

def temp_list(request):
    temps= Temp.objects.order_by('-created_date')
    return render(request, 'tempreture/temp_list.html', {'temps': temps})

def temp_detail(request, pk):
    temp = get_object_or_404(Temp, pk=pk)
    return render(request, 'tempreture/temp_detail.html',{'temp': temp})

def temp_new(request):
    if request.method == "POST":
        form = TempForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.author = request.user
            a.save()
            return redirect('temp_detail', pk=a.pk)
    else:
        form = TempForm()
    return render(request, 'tempreture/temp_edit.html', {'form':form})

def temp_edit(request, pk):
    temp = get_object_or_404(Temp, pk=pk)
    if request.method == "POST":
        form = TempForm(request.POST, instance=temp)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
            return redirect('temp_detail', pk=temp.pk)
    else:
        form = TempForm(instance=temp)
    return render(request, 'tempreture/temp_edit.html', {'form': form})