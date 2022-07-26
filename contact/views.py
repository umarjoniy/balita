from django.shortcuts import render, redirect
from .forms import FormContact


def contact(request):
    form = FormContact(request.POST or None)
    if form.is_valid():
        form.save()

    if request.method == 'POST':
        return redirect('/contact')

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)
