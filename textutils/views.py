
# i have created this file(by chirag)

from django.http import HttpResponse

from django.shortcuts import render # for template

# # code for video 6 
# def index(request):
#     return HttpResponse("<h1>hello chirag</h1>")

# def about(request):
#     return HttpResponse("about chirag")

# def navigate(request):
#     s = '''<h2>Navigation Bar<br></h2>
#         <a href="https://www.facebook.com/">facebook</a><br>
#         <a href="https://www.flipkart.com/">flipkart</a><br>
#         <a href="https://www.google.com/">google</a><br>'''
#     return HttpResponse(s)

# # code for video 7 and 8 too
def index(request):
    return render(request,'index.html')#for template
    # return HttpResponse("Home")

# def removepunc(request):
#     #get the text
#     djtext = request.GET.get('text','default')
#     print(djtext)# Analyze the text
#     return HttpResponse("remove punc")


# for video 10
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #Check which checkbox is on
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text 
        # return render(request, 'analyze.html', params)
    
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text 
        # return render(request, 'analyze.html', params)
   
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):#enumerate for line no.
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        
        params = {'purpose':'removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text 
        # return render(request, 'analyze.html', params)
   
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!= "\n" and char!="\r":
                analyzed = analyzed + char
        
        params = {'purpose':'removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text 
        # return render(request, 'analyze.html', params)
    
    if(charcount == "on"):
        analyzed = len(djtext),"this is no. of character"
        params = {'purpose':'number of character', 'analyzed_text': analyzed}
        djtext = analyzed
        # analyze the text 
        # return render(request, 'analyze.html', params)
   
    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("you didn't select any operation")

    return render(request, 'analyze.html', params)



# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")

# def spaceremove(request):
#     return HttpResponse("space remover back")

# def capitalizefirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("charcount")