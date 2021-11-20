from django.shortcuts import render
from django.http import HttpResponse
from .models import Part, Chapter
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(request):
    part_details = Part.objects.all()
    chap_details = []
    chap_d = {}
    count = len(chap_d)
    for part in part_details:
        chapter = Chapter.objects.filter(chapter=part.id)
        print(chapter)
        for chap in chapter:
            chap_details.append(chap)
            
        chap_d[count] = {'part': part, 'chap': chap_details}
        count += 1
        chap_details = []
    return render(request, 'kcweblayout/home.html', {'chap_d': chap_d})

def topic_detail(request, part_num, chap_num):
    part = get_object_or_404(Part, pk=part_num)
    chapter = get_object_or_404(Chapter, pk=chap_num)
    return render(request, 'kcweblayout/topic_detail.html', {'part': part, 'chap': chapter})
