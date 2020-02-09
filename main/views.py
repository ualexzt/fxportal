import os
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect

from main.forms import ContactForm


def main_index(request):
    return render(request, 'main/index.html')


def contact(reguest):
    sent = False
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            cd = form.cleaned_data
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            subject = 'Новое письмо от {}'.format(cd['firstname']+' '+cd['lastname'])
            sender = form.cleaned_data['sender']
            message = 'Прислал {}. Пишет: {}'.format(cd['sender'], cd['message'])
            recipients = ['ualexzt@gmail.com']
            send_mail(subject, message, sender, recipients)
            # Переходим на другую страницу, если сообщение отправлено
            sent = True

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'main/contact.html', {'form': form, 'sent': sent})


def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cmedata', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
