from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from .forms import UserLoginForm, UserRegisterForm, CreateProfileForm
from .models import Examinee, Examiner, Verification
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from .models import Profile
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib.auth.models import User

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/dashboard')

    context = {
        'form': form,
    }
    return render(request, "UserManagement/login.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        t = int(form.cleaned_data.get('role'))  # Return Index of Choice
        # print('REST:', t)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user.set_password(password)
        user.is_active = False
        user.save()
        #print(username, password, email)
        # user = get_user_model().objects.create(username=username, password=password, email=email)
        s_uuid = str(uuid.uuid4()) + "-" + username
        verify = Verification(user=user, uid=s_uuid)
        verify.save()
        rec_mail = [email]
        status = send_mail(
            subject="Welcome to Online Quiz Platform",
            message=str('Hello!' + username),
            from_email=getattr(settings, "EMAIL_HOST_USER"),
            recipient_list=rec_mail,
            fail_silently=True,
            html_message=render_to_string('mail_body.html', {'s_uuid': s_uuid,
                                                             'user': user.get_full_name()})
        )

        if status == 1:

            user_message = 'Email sent successfully. Please enter the verification code.'
            context = {
                'message': user_message,
            }
            print(user_message)

            # return redirect('verification')
        else:
            user_message = 'Failed! Try again please!'
            print(user_message)

        #new_user = authenticate(username=user.username, password=password)
        if t == 1:
            # print('It Works')
            examinee = Examinee(user=user, organization=form.cleaned_data.get('organization'))
            examinee.save()
        if t == 2:
            # print('It Works')
            examiner = Examiner(user=user, organization=form.cleaned_data.get('organization'))
            examiner.save()
        #login(request, new_user)
        #if next:
            #return redirect(next)
        logout(request)
        context = {
            'email': email,
            'username': user.get_full_name(),
        }
        return render(request,'UserManagement/verification.html',context)

    context = {
        'form': form,
    }
    return render(request, "UserManagement/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def user_dash(request):
    if request.user.is_authenticated:
        examinee = Examinee.objects.filter(user=request.user)
        examiner = Examiner.objects.filter(user=request.user)
        if examinee:
            context = {
                "user": request.user,
                "examinee": True,
            }
        else:
            context = {
                "user": request.user,
                "examiner": True
            }

        return render(request, 'UserManagement/user_dash_base.html', context)
    else:
        return redirect('/')


# def show_all_user(request):
#     examinee = Examinee.objects.all()
#     examiner = Examiner.objects.all()
#     context = {
#         'examiner': examiner,
#         'examinee': examinee
#     }
#     return render(request, 'UserManagement/show_all_user.html', context)
@login_required
def create_profile(request):
    form = CreateProfileForm()
    if request.method == "POST":
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
    context = {
        'form': form,
    }
    return render(request, "UserManagement/createprofile.html", context)


@login_required
def show_profile(request):
    examiner = Examiner.objects.filter(user=request.user)
    if examiner:
        examiner = True
    profile = Profile.objects.filter(user=request.user)
    if profile:
        context = {
            'examiner': examiner,
            'profile': profile[0],
        }
        return render(request, "UserManagement/showprofile.html", context)
    context = {
        'examiner': True,
        'message': "You Didn't Create Profile",
    }
    return render(request, "UserManagement/noprofile.html", context)


def verify_account(request, uid):
    user_ = Verification.objects.get(uid=uid)
    user = User.objects.filter(id=user_.user.id).update(is_active=True)
    username= user_.user.get_full_name
    user_.delete()
    context={
        'username': username
    }
    return render(request,'UserManagement/verification_success.html', context)





#For Debugging
# def test(request):
#     return  render(request,'UserManagement/verification_success.html')