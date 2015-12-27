from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

from .models import Profile
from .forms import ProfileForm


def ProfileCreate(request):
    template="profile.html"
    context={}
    if request.user.get_username()=='':
        return redirect('account_login')
    if Profile.objects.all().filter(user__username=request.user.get_username()).count()>0:
        return redirect('chatbot')
    else:
        form = ProfileForm(request.POST  or None ,request.FILES or None )

        if form.is_valid():

            new_profile = form.save(commit=False)
            
            user = User.objects.all().filter(username=request.user.get_username())[0]
            new_profile.user=user
            new_profile.save()
            form.save_m2m()
            return redirect('chatbot')

        context['form']=form

        
    return render(request,template,context)

# class ProfileCreate(UpdateView,LoginRequiredMixin):
 
        # if Profile.objects.all().filter(user__username=self.request.user).count()>0
        # return redirect('chatbot')
    # def __init__(self):
        # Profile.objects.all().filter(user__username=username).count()>0
        # print(username)
    # model = Profile
    # template_name ="profile.html"
    # fields = ['avatar','city','fav_food','relationship','preferrs']

    # def form_valid(self,form):
    #     form.instance.user=self.request.user
    #     # print(instance)
    #     return super(ProfileCreate,self).form_valid(form)

	# def form_valid(self,form):
	# 	form.instance.user = self.request.user
	# 	return super(ContactView, self).form_valid(form)
        

# def profile(request):
# 	template="profile.html"
# 	context={}

# 	return render(request,template,context)