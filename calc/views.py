# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request): #when you request the home page the urls.py will allow views to call the home function which accepts request as an arguement, and the home function returns the hello world as an httpresponse
    #you will use render the requested file because the function is now returning a dynamic page not just a text
    return render(request, "index.html",{"name":"i-wizard"})

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=int(request.POST['num6'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc6=int(request.POST['sco6'])
    total_val_add =(val1+val2+val3+val4+val5+val6)
    total_val =(val1,val2, val3, val4, val5, val6)
    total_sc = (sc1, sc2, sc3, sc4, sc5, sc6)
    total_val_sc = 0
    for i in range(6):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})


def fourth(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    total_val_add =(val3+val4+val1+val2)
    total_val =(val3, val4, val1, val2)
    total_sc = (sc3, sc4, sc1, sc2)
    total_val_sc = 0
    for i in range(4):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})
def fifth(request):
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val1=int(request.POST['num1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc1=int(request.POST['sco1'])
    total_val_add =(val2+val3+val4+val5+val1)
    total_val =(val2, val3, val4, val5, val1)
    total_sc = (sc2, sc3, sc4, sc5, sc1)
    total_val_sc = 0
    for i in range(5):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})
def seventh(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=int(request.POST['num6'])
    val7=int(request.POST['num7'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc6=int(request.POST['sco6'])
    sc7=int(request.POST['sco7'])
    total_val_add =(val1+val2+val3+val4+val5+val6+val7)
    total_val =(val1,val2, val3, val4, val5, val6, val7)
    total_sc = (sc1, sc2, sc3, sc4, sc5, sc6, sc7)
    total_val_sc = 0
    for i in range(7):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})


def eighth(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=int(request.POST['num6'])
    val7=int(request.POST['num7'])
    val8=int(request.POST['num8'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc6=int(request.POST['sco6'])
    sc7=int(request.POST['sco7'])
    sc8=int(request.POST['sco8'])
    total_val_add =(val1+val2+val3+val4+val5+val6+val7+val8)
    total_val =(val1,val2, val3, val4, val5, val6, val7, val8)
    total_sc = (sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8)
    total_val_sc = 0
    for i in range(8):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})


def ninth(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=int(request.POST['num6'])
    val7=int(request.POST['num7'])
    val8=int(request.POST['num8'])
    val9=int(request.POST['num9'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc6=int(request.POST['sco6'])
    sc7=int(request.POST['sco7'])
    sc8=int(request.POST['sco8'])
    sc9=int(request.POST['sco9'])
    total_val_add =(val1+val2+val3+val4+val5+val6+val7+val8+val9)
    total_val =(val1,val2, val3, val4, val5, val6, val7, val8, val9)
    total_sc = (sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8, sc9)
    total_val_sc = 0
    for i in range(9):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})

def tenth(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=int(request.POST['num6'])
    val7=int(request.POST['num7'])
    val8=int(request.POST['num8'])
    val9=int(request.POST['num9'])
    val10=int(request.POST['num10'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc6=int(request.POST['sco6'])
    sc7=int(request.POST['sco7'])
    sc8=int(request.POST['sco8'])
    sc9=int(request.POST['sco9'])
    sc10=int(request.POST['sco10'])
    total_val_add =(val1+val2+val3+val4+val5+val6+val7+val8+val9+val10)
    total_val =(val1,val2, val3, val4, val5, val6, val7, val8, val9, val10)
    total_sc = (sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8, sc9, sc10)
    total_val_sc = 0
    for i in range(10):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})

def eleventh(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=int(request.POST['num3'])
    val4=int(request.POST['num4'])
    val5=int(request.POST['num5'])
    val6=int(request.POST['num6'])
    val7=int(request.POST['num7'])
    val8=int(request.POST['num8'])
    val9=int(request.POST['num9'])
    val10=int(request.POST['num10'])
    val11=int(request.POST['num11'])
    sc1=int(request.POST['sco1'])
    sc2=int(request.POST['sco2'])
    sc3=int(request.POST['sco3'])
    sc4=int(request.POST['sco4'])
    sc5=int(request.POST['sco5'])
    sc6=int(request.POST['sco6'])
    sc7=int(request.POST['sco7'])
    sc8=int(request.POST['sco8'])
    sc9=int(request.POST['sco9'])
    sc10=int(request.POST['sco10'])
    sc11=int(request.POST['sco11'])
    total_val_add =(val1+val2+val3+val4+val5+val6+val7+val8+val9+val10+val1)
    total_val =(val1,val2, val3, val4, val5, val6, val7, val8, val9, val10, val11)
    total_sc = (sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8, sc9, sc10, sc11)
    total_val_sc = 0
    for i in range(11):
        val = total_val[i]
        sc = total_sc[i]
        val_sc = val * sc
        total_val_sc += val_sc
    result1 = total_val_sc/total_val_add
    result = round(result1, 2)
    
    #res= val1 + val2
    if result>=4.5:
        messages.info(request, "Status: First Class")
        messages.info(request, "Remark: Genius, your skills are excellent and God-like!")
        return render(request, "index.html",{"result":result})
    elif result<=4.49 and result>=3.5:
        messages.info(request, "Status: Second Class Upper")
        messages.info(request, "Remark: Great job, you are a professional in your field")
        return render(request, "index.html",{"result":result})
    elif result<=3.49 and result>=2.5:
        messages.info(request, "Status: Second Class Lower")
        messages.info(request, "Remark: Good job, you are on a good path but you can do better")
        return render(request, "index.html",{"result":result})
    elif result<=2.49 and result>=1.5:
        messages.info(request, "Status: Third Class")
        messages.info(request, "Remark: Warning, serious improvement is needed")
        return render(request, "index.html",{"result":result})
    else:
        messages.info(request, "Status: Pass")
        messages.info(request, "Remark: Your score is very low, you need help urgently!")
        return render(request, "index.html",{"result":result})

