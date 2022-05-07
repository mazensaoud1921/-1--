import json
def Quiz():
    name=["mazen","saoud"]
    score=[]
    i=0
    while(i<=1):
        
        mark=0
        student=input("أدخل اسم الطالب--->:"+str(name[i]))
        i+=1
        m1=input ("السؤال الأول؟")
        m2=input ("السؤال الثاني؟")
        m3=input ("السؤال الثالث؟")
        m4=input ("السؤال الرابع؟")
        m5=input ("السؤال الخامس؟")
        m6=input ("السؤال السادس؟")
        m7=input ("السؤال السابع؟")
        m8=input ("السؤال الثامن؟")
        m9=input ("السؤال التاسع؟")
        m10=input ("السؤال العاشر؟")
        m11=input ("السؤال الحادي عشر؟")
        m12=input ("السؤال الثاني عشر؟")
        m13=input ("السؤال الثالث عشر؟")
        m14=input ("السؤال الرابع عشر؟")
        m15=input ("السؤال الخامس عشر؟")
        m16=input ("السؤال السادس عشر؟")
        m17=input ("السؤال السابع عشر؟")
        m18=input ("السؤال الثامن عشر؟")
        m19=input ("السؤال التاسع عشر؟")
        m20=input ("السؤال العشرون؟")
        #(على فرض الأسئلة مؤتمتة يتم اختيار)
        #a---> للصح
        #b---> للخطأ
        if m1=="a":
            mark+=1
        else:
            mark+=0
        if m2=="b":
            mark+=1
        else:
            mark+=0
        if m3=="a":
            mark+=1
        else:
            mark+=0
        if m4=="a":
            mark+=1
        else:
            mark+=0
        if m5=="b":
            mark+=1
        else:
            mark+=0
        if m6=="b":
            mark+=1
        else:
            mark+=0
        if m7=="b":
            mark+=1
        else:
            mark+=0
        if m8=="a":
            mark+=1
        else:
            mark+=0
        if m9=="a":
            mark+=1
        else:
            mark+=0
        if m10=="b":
            mark+=1
        else:
            mark+=0
        if m11=="a":
            mark+=1
        else:
            mark+=0
        if m12=="b":
            mark+=1
        else:
            mark+=0
        if m13=="a":
            mark+=1
        else:
            mark+=0
        if m14=="a":
            mark+=1
        else:
            mark+=0
        if m15=="b":
            mark+=1
        else:
            mark+=0
        if m16=="a":
            mark+=1
        else:
            mark+=0
        if m17=="a":
            mark+=1
        else:
            mark+=0
        if m18=="a":
            mark+=1
        else:
            mark+=0
        if m19=="b":
            mark+=1
        else:
            mark+=0
        if m20=="b":
            mark+=1
        else:
            mark+=0
        print("العلامة هي--->:"+str(mark))
        score.append(mark)

    dic={}
    i=0
    while (i<=1):
        xname=name[i]
        mark=score[i]
        dic[xname]={"the name":xname,"the mark":mark}
        i+=1
    mmm=json.dumps(dic)
    with open ("mazen.json","w") as m:
        m.write(mmm)
    with open ("mazen.json","r") as m:
        x=json.loads(m.read())
    print (x)
