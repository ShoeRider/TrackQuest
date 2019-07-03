from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.models import User

from .models import Friend,FriendRequest,Profile
from .admin import UserCreationForm
from .forms import LogIn_Form

    #Used By: SignUp



class Dashboard(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'dashboard.html'

def View_Site_Dashboard(request):
    context = {}

    return render(request, 'Site_Dashboard.html', context)
    #return render(request, 'dashboard.html', {"from": "coming soon !"})




def Base(request):
    return render(request, 'Base.html')


def view_user(request,username):
    context = {}
    context['User'] = User.objects.get(username=username)
    context['Prof'] = Profile.objects.filter(user_pk=context['User'])
    print(context['Prof'])
    #if(context['Prof'])
    if(context['Prof'].count() == 0):
        Profile.make_profile(user_pk=context['User'])
        context['Prof'] = Profile.objects.filter(user_pk=context['User'])[0]
    else:
        context['Prof'] = Profile.objects.filter(user_pk=context['User'])[0]
    print(context['Prof'])
    if(username == request.user.username):
        context['User_Prof'] = True
    if(User):
        #return render(request, 'friend/FormFill_FriendRequest.html', {"from": "you cannot friend yourself !"})
        return render(request, 'Users/DetailedUser.html',context)
    return render(request, '404.html', {"from": "coming soon !"})
    #return render(request, 'friend/FormFill_FriendRequest.html', {"from": "coming soon !"})

################################################################################
#Account Management
################################################################################

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'Users/SignUp.html'

class EditProfile(generic.edit.UpdateView):
    context = {}
    #context["Profile"] =
    model = Profile
    fields = ['name','pic','email','bio','affiliation']
    template_name = 'users/Update_Profile.html'
    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(**kwargs)

        obj = super(UpdateProfile, self).get_object(*args, **kwargs)
        data['User_Prof'] = True
        if not obj.user_pk == self.request.user:
            data['User_Prof'] = False

        return data

def LogOut(request):
    logout(request)
    return render(request, 'Base.html')
    # Redirect to a success page.


def LogIn(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Base.html')
        else:
            return render(request, 'Base.html')
    context["LogIn_Form"] = LogIn_Form()
    return render(request, 'Users/LogIn.html',context)
