from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.customer import forms

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@login_required()
def home(request):
    return redirect(reverse('customer:profile'))

@login_required(login_url='/sign_in/?next=/customer/')
def profile_page(request):
    customer_forms = forms.BasicCustomerForm(instance=request.user.customer)
    password_form = PasswordChangeForm(request.user)

    user_forms = forms.BasicUserForm(instance=request.user)

    if request.method == 'POST':

        if request.POST.get('action') == 'update_profile':
            user_forms = forms.BasicUserForm(request.POST, instance=request.user)
            customer_forms = forms.BasicCustomerForm(request.POST, request.FILES, instance=request.user.customer)

            if user_forms.is_valid() and customer_forms.is_valid():
                user_forms.save()
                customer_forms.save()

                messages.success(request, 'Profile updated successfully')
                return redirect(reverse('customer:profile'))
        
        elif request.POST.get('action') == 'update_password':
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password updated successfully')
                return redirect(reverse('customer:profile'))


    return render(request, 'customer/profile.html',
                   {'user_forms': user_forms,
                    'customer_forms': customer_forms,
                    "password_form": password_form,})
    


#please add comments to the all function because this is a complex app