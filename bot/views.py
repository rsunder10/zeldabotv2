from bot.aiml.Kernel import Kernel
import sys
import ast
import random
from django.shortcuts import render,render_to_response
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from django.views.generic import TemplateView
from user.models import Profile,Zelda
from .models import RestaurantBasic,Menu
from user.mixins import LoginRequiredMixin
from .models import ContactUs



# Create your views here.
def home(request):
    template="home.html"
    context = {}
    return render(request,template,context)

# About us page function
def about(request):
    template="about.html"
    context={}
    return render(request,template,context)
#Contact Us Page Function


class Contact(CreateView):
    template_name = 'contact.html'
    model = ContactUs
    fields = ['name','subject','email','detail']
    
# @login_required(redirect_field_name='account_login')
class Bot(LoginRequiredMixin,TemplateView):

    template_name = "chatbot.html"

    def get_context_data(self, **kwargs):
        context = super(Bot, self).get_context_data(**kwargs)
        if self.request.user.get_username()!='':   
            context['user']=Profile.objects.all().filter(user__username=self.request.user)[0].avatar
        context['zelda']=Zelda.objects.all()[0].avatar
        return context


    def get(self, request, *args, **kwargs):
        msg = request.GET.get("msg",None)
        context = self.get_context_data()
        food_template_ans = ['We have found','We were able to find','Our search resultant in finding',]
        insufficient_template =['Either Input What You Need To Eat or Restaurant Name In a Phrase',]
        
        if msg:
            
            kern = Kernel()
            kern.setBotPredicate('name', 'Zelda')
            kern.setBotPredicate('master', 'Sunder')

    
            brainLoaded = False
            forceReload = False

            while not brainLoaded:
                if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
                    
                    kern.bootstrap(learnFiles="bot/std-startup.xml", commands="load aiml b")
                    
                    brainLoaded = True
                    
                    kern.saveBrain("bot/standard.brn")

                else:
                    try:
                        
                        kern.bootstrap(brainFile = "bot/standard.brn")


                        brainLoaded = True
                    except:
                        forceReload = True
            while(True):
                raw_reply=kern.respond(msg)
                # print(raw_reply[1:])
                # if raw_reply[0]==$:
                print(raw_reply[0])



                if raw_reply[0]=='~':
                    area=None
                    cheap=None   
                    rest=None
                    food=None
                    lists=None                 
                    processed_reply = raw_reply[1:]

                    print(ast.literal_eval(processed_reply))
                    query = ast.literal_eval(processed_reply)
                    for k,v in query.items():
                        if(k=='area'):
                            area = v
                        if(k=='cheap'):
                            cheap =v
                        if(k=='rest'):
                            rest=v
                        if(k=='food'):
                            food =v
                        if(k=='list'):
                            lists=v
                    print(area)
                    print(rest)
                    print(food)
                    print(cheap)
                    print(lists)
                    if area != None and cheap=='True':
                        best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('retaurant_basic__cost')[0]
                        template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                        return JsonResponse({'reply':template})
                    if area != None and cheap=='False':
                        best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__cost')[0]
                        template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                        return JsonResponse({'reply':template})
                    if rest!=None:
                        print(rest)
                        best = Menu.objects.all().filter(retaurant_basic__r_name__contains=rest).order_by('-retaurant_basic__rating')[0]
                        print(best)
                        template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Address: <b>'+best.retaurant_basic.r_address+'</b></li><br/></ul></div></div>'
                        return JsonResponse({'reply':template})
                    if food!=None and cheap =='True':
                        print('hi')
                        best = Menu.objects.all().filter(food__food_name=food).order_by('food__price')[0]
                        print(best)
                        price =best.food.get(food_name=food).price
                        

                        template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Food:'+food+'</li><li>Price: <b>'+str(price)+'</b></li><li>Address: <b>'+best.retaurant_basic.r_address+'</b></li><br/></ul></div></div>'
                        return JsonResponse({'reply':template})

                    if food!=None and cheap =='False':
                        best = Menu.objects.all().filter(food__food_name=food).order_by('-food__price')[0]
                        price =best.food.get(food_name=food).price
                        print(best)
                        template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Food:'+food+'</li><li>Price: <b>'+str(price)+'</b></li><li>Address: <b>'+best.retaurant_basic.r_address+'</b></li><br/></ul></div></div>'
                        return JsonResponse({'reply':template})

                    if area!=None and lists=='True':
                        list_rate = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__rating')

                        template=''
                        for best in list_rate:
                            template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                        return JsonResponse({'reply':template})

                if raw_reply[0]=='$':
                    processed_reply=raw_reply[1:]
                    # reply_dict = dict(list(processed_reply))
                    print(processed_reply)
                    print(ast.literal_eval(processed_reply))
                    query =ast.literal_eval(processed_reply)
                    for k,v in query.items() :
                        if(k=='food'):
                            request.session['food']=v
                            request.session['r_cuisine']=None
                            request.session['area']=None                            
                        if(k=='rcuisine'):
                            request.session['r_cuisine']=v
                            request.session['food']=None
                            request.session['area']=None
                        if(k=='restaurant'):
                            request.session['r_name']=v
                        if(k=='area'):
                            request.session['area'] =v
                            request.session['food']=None
                            request.session['r_cuisine']=None


                    area =request.session.get('area')
                    food = request.session.get('food')
                    r_name =request.session.get('r_name')
                    cuisine = request.session.get('r_cuisine')
                    
                    
                    if food != None:
                        count = Menu.objects.all().filter(food__food_name=food).count()

                        
                        bot_template =random.choice(food_template_ans)
                        response =bot_template+" "+str(count)+" "+'restaurants'
                        # print(response)
                        return JsonResponse({'reply':response})
                    if cuisine != None:
                        count = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).count()                  
                        bot_template =random.choice(food_template_ans)
                        response =bot_template+" "+str(count)+" "+'restaurants'
                        # print(response)
                        return JsonResponse({'reply':response})
                    if area != None:
                        
                        count = Menu.objects.all().filter(retaurant_basic__area__contains=area).count()
                        bot_template =random.choice(food_template_ans)
                        response=bot_template + " "+str(count)+" "+'restaurants'
                        return JsonResponse({'reply':response})

                if raw_reply[0]=='+':
                    processed_reply=raw_reply[1:]
                    #based on the rating
                    if processed_reply =='rating':
                        print( request.session.get('r_name')==None)
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine')==None and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})
                            
                        if request.session.get('food'):
                            food=request.session.get('food')
                            best = Menu.objects.all().filter(food__food_name=food).order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})                            
                        #for the restaurant

                    if processed_reply == 'bmaps':
                        print('hi')
                        
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine')==None and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})

                        if request.session.get('food'):
                            print('hi')
                            food=request.session.get('food')
                            best = Menu.objects.all().filter(food__food_name=food).order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})                            


                    #show the list
                    if processed_reply =='list':
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine')==None and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})

                        if request.session.get('food'):
                            food = request.session.get('food')                     
                            list_rate = Menu.objects.all().filter(food__food_name=food).order_by('-retaurant_basic__rating')
                            print(list_rate)
                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            list_rate = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('-retaurant_basic__rating')

                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            list_rate = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__rating')

                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})


                    if processed_reply =='lmaps':
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine')==None and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})

                        if request.session.get('food'):
                            food = request.session.get('food')                     
                            list_rate = Menu.objects.all().filter(food__food_name=food).order_by('-retaurant_basic__rating')
                            print(list_rate)
                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            list_rate = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('-retaurant_basic__rating')

                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            list_rate = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__rating')

                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})
                        #for the restaurant

                    if processed_reply =='cheap':
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine')==None and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})
                        if request.session.get('food'):
                            food=request.session.get('food')

                            best = Menu.objects.all().filter(food__food_name=food).order_by('retaurant_basic__cost')[0]
                            print(best)
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('retaurant_basic__cost')[0]
                            
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})                               




                    if processed_reply =='cmaps':
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine')==None and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})
                        if request.session.get('food'):
                            food=request.session.get('food')

                            best = Menu.objects.all().filter(food__food_name=food).order_by('retaurant_basic__cost')[0]
                            print(best)
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('retaurant_basic__cost')[0]
                            
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template}) 


                    if processed_reply =='cosmaps':
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine') and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})
                        if request.session.get('food'):
                            food=request.session.get('food')
                            best = Menu.objects.all().filter(food__food_name=food).order_by('-retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})                                            

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('-retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><iframe width="450" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='+best.retaurant_basic.r_name+'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe><br/></div></div>'
                            return JsonResponse({'reply':template}) 



                        #for the restaurant

                    if processed_reply =='costly':
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine') and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})
                        if request.session.get('food'):
                            food=request.session.get('food')
                            best = Menu.objects.all().filter(food__food_name=food).order_by('-retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})                                            

                        if request.session.get('r_cuisine'):
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).order_by('-retaurant_basic__cost')[0]
                            template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):
                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).order_by('-retaurant_basic__cost')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template}) 
                        #for the restaurant
                
                    if processed_reply=='bveg':
                        print(request.session.get('area'))
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine') and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})                                         

                        if request.session.get('r_cuisine'):
                        
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).filter(food__food_name__contains='veg').order_by('-retaurant_basic__rating')[0]
                            template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):

                            area = request.session.get('area')
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).filter(food__food_name__contains='veg').order_by('-retaurant_basic__rating')[0]
                            template ='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Cost:'+str(best.retaurant_basic.cost)+'</li><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div>'
                            return JsonResponse({'reply':template})                     

                    if processed_reply=='lveg':
                        print(request.session.get('area'))
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine') and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})                                         

                        if request.session.get('r_cuisine'):
                        
                            cuisine = request.session.get('r_cuisine')
                            list_rate = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).filter(food__food_name__contains='veg').order_by('-retaurant_basic__rating')
                            template=''
                            for best in list_rate:

                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})

                        if request.session.get('area'):

                            area = request.session.get('area')
                            list_rate = Menu.objects.all().filter(retaurant_basic__area__contains=area).filter(food__food_name__contains='veg').order_by('-retaurant_basic__rating')
                            template=''
                            for best in list_rate:
                                template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                            return JsonResponse({'reply':template})

                    if processed_reply=='lnon':
                        print('his')
                        if request.session.get('food')==None and request.session.get('r_name')==None and request.session.get('r_cuisine') and request.session.get('area')==None:
                            return JsonResponse({'reply':random.choice(insufficient_template)})                                         

                        if request.session.get('r_cuisine'):
                        
                            cuisine = request.session.get('r_cuisine')
                            best = Menu.objects.all().filter(retaurant_basic__cuisines__contains=cuisine).filter(food__food_name__contains='chicken')
                            if(best.count() == 0):
                                return JsonResponse({'reply':'There is No Non Veg Restaurant Found'})
                            else:
                                list_rate=best.order_by('-retaurant_basic__rating')
                                template=''
                                for best in list_rate:
                                    template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                                    return JsonResponse({'reply':template})  

                        if request.session.get('area'):

                            area = request.session.get('area')
                            print(area)
                            best = Menu.objects.all().filter(retaurant_basic__area__contains=area).filter(food__food_name__contains='chicken')
                            print(best)
                            if(best.count() == 0):
                                return JsonResponse({'reply':'There is No Non Veg Restaurant Found'})
                            else:
                                list_rate=best.order_by('-retaurant_basic__rating')
                                template=''
                                for best in list_rate:
                                    template +='<div class="switch-right-grid"><div class="switch-right-grid1"><h3 style="margin-top: 0px;">'+best.retaurant_basic.r_name+'('+best.retaurant_basic.r_type+')</h3><p>'+best.retaurant_basic.cuisines+'</p><br/><ul><li>Rating:'+str(best.retaurant_basic.rating)+'</li><li>Rating Votes:'+str(best.retaurant_basic.rating_votes)+'</li><li>Address: '+best.retaurant_basic.r_address+'</li><br/></ul></div></div><br/><br/>'
                                    return JsonResponse({'reply':template})    
                            
                    # processed_reply = raw_reply[1:]
                    # print(processed_reply)

                        
                return JsonResponse({'reply': raw_reply})
        return self.render_to_response(context)



# google Api
# <iframe width="600" height="450" frameborder="0" style="border:0"src="https://www.google.com/maps/embed/v1/place?q='.$result_addr.'&key=AIzaSyCFXDb1zQ6MFKvHA3uHQjJOS-w64xyfcTc" allowfullscreen></iframe>