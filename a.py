list=["مازن","عمار","ماهر","علاء","محمد","أحمد","فارس"]
i=1
while(i!=10):
    name=input ("أدخل اسم الطالب--->:")
    if name in list:
        print ("الطالب متخرج")

    else:
        print("الطالب غير متخرج")
