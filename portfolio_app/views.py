from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # AJAX request
                return JsonResponse({'success': True})
            return redirect('index')  # Redirect on successful non-AJAX POST
        else:
            return render(request, 'index.html', {'form': form})

    form = ContactForm()
    return render(request, 'index.html', {'form': form})

def view_messages(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == settings.VIEW_MESSAGES_PASSWORD:
            messages = Message.objects.all().order_by('-timestamp')
            return render(request, 'view_messages.html', {'messages': messages})
        else:
            return render(request, 'view_messages.html', {'error': 'Incorrect password'})

    return render(request, 'view_messages.html')
