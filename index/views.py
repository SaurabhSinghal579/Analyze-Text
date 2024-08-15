# author - Saurabh
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def result(request):
    djtext=request.POST.get('text','default') # get the text coming from template
    length=request.POST.get('length','off') 
    lower=request.POST.get('lower','off') 
    upper=request.POST.get('upper','off') 
    title=request.POST.get('title','off') 
    if djtext!="":
        if (length == "on" or lower=="on" or upper=="on" or title=="on"):
            if length =='on':
                length1=len(djtext)
                params={'analyzed_text':length1}
            if lower =='on':
                lower1=djtext.lower()
                params={'analyzed_text':lower1}
                djtext=lower1
            if upper =='on':
                upper1=djtext.upper()
                params={'analyzed_text':upper1}
            if title =='on':
                title1=djtext.title()
                params={'analyzed_text':title1}
            return render(request, 'result.html',params) 
        else:
            return HttpResponse("Please choose atleast one option")
    else:
        return HttpResponse("Please enter text")