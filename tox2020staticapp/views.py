from django.shortcuts import render
# Create your views here.
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
def index(request):
    success = 0
    if request.POST:
        success =1
        j = 0
        email_id = request.POST['email']
        fr = open('Subscription_List/subscribers.txt','r')
        fw = open('Subscription_List/subscribers.txt','a')
        for i in fr:
            if i == email_id:
                j = 1
                return HttpResponse('<h1><br><br>You are already subscribed to our mailing list. Thank you for showing interest in TOX2020 once again.</h1>')
        if j == 0:
                fw.write('\n' + email_id)
        # email = EmailMessage("Admin @ TOX2020 | Hello Sir/Ma'am\n Thank you for showing interest in TOX2020. \n You will be notified once our system is live.\n\nAdmin,\nTox2020.co.in", from_email=['admin@tox2020@co.in'],to=[str(email_id)])
                subject = "TOX2020 Launching soon!!!"
                message = "Hello Sir/Ma'am,\n\nThank you for your interest in TOX2020 web service. We will notify you once our website is live.\n\nAdmin,\nTOX2020.co.in\n"
                from_email = settings.EMAIL_HOST_USER
                to_list = [str(email_id)]
                try:
            # attach_file()
                    send_mail(subject,message, from_email, to_list, fail_silently = False)
                except:
                    return HttpResponse("Some error occurred while sending mail. Contact admin@tox2020.co.in")
        # email.send(fail_silently = False)
    if success == 0:
        return render(request, "index.html")#, locals())
    elif success == 1 and j==0:
        return HttpResponse("<h1><br><br><br><br><center>Successful</center></h1>")
def success(request):
    index(request)
    success = 1
    return render(request,'index.html')