from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.customer import forms

@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

@login_required(login_url='/sign_in/?next=/customer/')
def profile_page(request):
    user_forms = forms.BasicUserForm(instance=request.user)

    if request.method == 'POST':
        user_forms = forms.BasicUserForm(request.POST, instance=request.user)
        if user_forms.is_valid():
            user_forms.save()
            return redirect(reverse('customer:profile'))

    return render(request, 'customer/profile.html',
                   {'user_forms': user_forms})
    


#please add comments to the all function because this is a complex app