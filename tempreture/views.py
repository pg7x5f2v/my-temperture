from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Temp
from .forms import TempForm
from django.shortcuts import redirect

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