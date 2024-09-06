from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


# def about(request):
#     return HttpResponse("This is about akash gautam")
    

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')
    #Check Checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    
    #Check which checkbox is open
    if removepunc=="on":
          punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
          analyzed = ""
          for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char

          params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
          djtext=analyzed
        #   return render(request,'analyze.html',params)

    #Code for converting in Uppercase
    if(fullcaps == "on"):
          analyzed = ""
          for char in djtext:
              analyzed = analyzed + char.upper()

          params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
          djtext=analyzed

    #Code for Newline remover
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
             if char!="\n" and char!="\r":
                 analyzed = analyzed + char

        params = {'purpose':'Removed Newlines','analyzed_text':analyzed}
        djtext=analyzed
        
    #Code for Extra space remover
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
              if not (djtext[index]==" " and djtext[index+1]==" "):
                     analyzed = analyzed + char

     #Or we can write
        '''for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                 pass
            else:
                 analyzed = analyzed + char'''

              
        params = {'purpose':'Removed extraspaces','analyzed_text':analyzed}
        djtext=analyzed

    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("You have not selected any operation! Please select operation and try again")

    return render(request,'analyze.html',params)

    
