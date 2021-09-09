from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request, "index.html")


def introduction(request):
    return render(request, "introduction.html")


def management(request):
    return render(request, "management.html")


def directormessage(request):
    return render(request, "directors_msg.html")


def corecompetence(request):
    return render(request, "corecompetence.html")


def ourteam(request):
    return render(request, "ourteam.html")


def classIX(request):
    return render(request, "classIX.html")


def classX(request):
    return render(request, "classX.html")


def classXI(request):
    return render(request, "classXI.html")


def classXII(request):
    return render(request, "classXII.html")


def classXIIpass(request):
    return render(request, "classXIIpass.html")


def ibsbankcoaching(request):
    return render(request, "ibs-bank-coaching.html")


def result19_20(request):
    return render(request, "result-19-20.html")


def result18_19(request):
    return render(request, "result-18-19.html")


def result17_18(request):
    return render(request, "result-17-18.html")


def result16_17(request):
    return render(request, "result-16-17.html")


def result15_16(request):
    return render(request, "result-15-16.html")


def result14_15(request):
    return render(request, "result-14-15.html")


def result13_14(request):
    return render(request, "result-13-14.html")


def result12_13(request):
    return render(request, "result-12-13.html")


def result11_12(request):
    return render(request, "result-11-12.html")


def contactus(request):
    return render(request, "contactus.html")


def regnform(request):
    return render(request, "regnform.html")


def online_regnform_tutions(request):
    return render(request, "online_regnform_tutions.html")

def testimonials(request):
    return render(request,"testimonials.html")


def terms_and_conditions(request):
    return render(request, "terms_and_conditions.html")


def refund_policy(request):
    return render(request, "refund-policy.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def home_2(request):
    return render(request,"home_2.html")



'''def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        template = get_template('contactus2.txt')
        context = {'name':name,'email':email,'phone':phone,'message':message}
        content = template.render(context)
        email = EmailMessage(
            "contact from recieved",
            content,
            "contact from "+'',
            ['envvumarketing3@gmail.com','envvumarketing6@gmail.com'],
            headers = {'Reply to ':email}

        )
        email.send()
        messages.success(request,+'thank you for contacting us')
    return render(request,'contactus.html')'''


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')


        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
        }
        print(data)

        message = '''

         Name: {}

         Email: {}

         phone: {}

         message: {}

        '''.format(data['name'], data['email'], data['phone'], data['message'])
        send_mail('ENQUIRY', message, '',
                  ['envvumarketing6@gmail.com','envvumarketing3@gmail.com'])

        html = "<html><body><br><br><h2>ThankYou For Submitting Registration form.</h2></body></html>"
        return HttpResponse(html)

    return render(request, "contactus.html", {})

