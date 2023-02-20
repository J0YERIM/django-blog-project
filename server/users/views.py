from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


# 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# 로그인

# 로그아웃

# 회원탈퇴

# 회원수정

# 회원 detail

# 회원 list

