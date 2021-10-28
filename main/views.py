from django.shortcuts import render, HttpResponseRedirect
from .models import Products, MainPicture
from django.core.mail import send_mail


def index(request):
    products = Products.objects.all()[:30]
    new_products = Products.objects.filter(new_products=True)
    main = MainPicture.objects.first()
    return render(request, 'index.html', {"products": products,
                                          "new_products": new_products,
                                          "main": main,
                                          })


def send_message(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = f'name: {name}\nphone: {phone}\nemail: {email}'
        print('_________________________________________________________________________________')
        print(message)
        # mail = send_mail('Granat-Vladivostok', message, 'admin@igorkhaylov.uz', ['admin@igorkhaylov.uz'], fail_silently=False, )
        # mail = send_mail('Granat-Vladivostok', message, 'totpravka@gmail.com', ['sonikry.99@gmail.com'], fail_silently=False, )
        mail = send_mail('Granat-Vladivostok', message, 'totpravka@gmail.com',
                         ['igorkhaylov@yandex.com', ], fail_silently=False, )
        if mail:
            print("Сообщение успешно отправлено")
        else:
            print("Ошибка отправки сообщения")
        return HttpResponseRedirect('/')



