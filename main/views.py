from django.shortcuts import render
from  main.models import Event, Email, Gal, Contact
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    e = Event.objects.all().order_by('event_date')[:5]
    img = Gal.objects.all().order_by('-created_at')
    context = {'e' : e, 'img' : img}
    print (e)
    return render(request, 'main/index.html', context)


@csrf_exempt
def add_mail(request):
    response_data = {}
    if request.method == "POST" and request.is_ajax:
        user_m = request.POST['mail']
        m = Email(email=user_m)
        m.save()
        response_data = {'Message': 'Success'}
    else:
        response_data = {'Message': 'Failed'}
    return JsonResponse(response_data)

@csrf_exempt
def contact(request):
    response_data = {}
    if request.method == "POST" and request.is_ajax:
        m = request.POST['mail']
        n = request.POST['name']
        s = request.POST['subject']
        msg = request.POST['message']
        mo = Contact(name = n, email = m, subject = s, message = msg)
        mo.save()
        response_data = {'Message': 'Ok'}
    else:
        response_data = {'Message': 'Failed'}
    return JsonResponse(response_data)

