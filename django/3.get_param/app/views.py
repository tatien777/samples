from django.http import HttpResponse

def login(request):
    name = request.GET.get('name','')
    request.sesion['name'] = name
    
def index(request): 
    name = request.session.get('name', '')
    return HttpResponse('Hello ' + name)
   
