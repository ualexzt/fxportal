from django.shortcuts import render, redirect
from .forms import UserCreateForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'profiles/register.html', {'form': form})


@login_required
def profile_main(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile_main')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'p_form': p_form,
        'u_form': u_form
    }
    return render(request, 'profiles/profile_main.html', context)


@login_required
def dashboard(request):
    return render(request, 'profiles/profile_dashboard.html')
