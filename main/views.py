from django.shortcuts import render
from .models import NC_skyField,FC_football_Center,Jangseong_Field
from sign.models import User
from django.shortcuts import redirect
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.db.models import F
from django.conf import settings
from football.settings import EMAIL_HOST_USER

# Create your views here.
def main(request):
        if request.method =="POST":
             match_day=request.POST["match_date"]
        
             NC_objects= NC_skyField.objects.filter(match_Date=match_day)
             FC_objects= FC_football_Center.objects.filter(match_Date=match_day)
             Jangseong_objects= Jangseong_Field.objects.filter(match_Date=match_day)
             data = {'NC':NC_objects,'FC':FC_objects,'Jangseong':Jangseong_objects}

   
             return render(request,'main/sorted_data.html',data)

        return render(request,'main/main.html')

def info_NC(request):
            
            if request.method=="POST":
                NC_skyField.objects.update(match_player=F('match_player')+1)
                NC_skyField.objects.update(match_level1=F('match_level1')+1)
                return redirect('/main/success')
            
            NC_objects=NC_skyField.objects.all()
            data = {'NC':NC_objects}
            return render(request,'main/info_NC.html',data)

def info_FC(request):
    return render(request,'main/info_FC.html')

def info_Jangseong(request):
    return render(request,'main/info_Jangseong.html')

def complete(request):
    user_email= User.email
    emailss = EmailMessage() 	#이메일 객체 생성
    emailss.subject = '박준용 메일 날라가유' 	#제목
    emailss.body = 'SMTP 구현' 	#부제목
    emailss.from_email = 'park000815@naver.com' #발신지
    emailss.to = [user_email] 			# 목적지
    emailss.send() 	
  
    return render(request,'main/complete.html')