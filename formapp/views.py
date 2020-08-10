from django.shortcuts import render
from formapp import forms

# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')


def form(request):
    form = forms.NewUser()

    if request.method == 'POST':
        form=forms.NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("Validation success of the post form!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("COLLEGE: " + form.cleaned_data['college'])
            return index(request)
        else:
            print("Error! Form Invalid.")

    return render(request, 'formapp/form.html', {'form':form})
