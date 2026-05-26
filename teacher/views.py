from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from teacher.models import Student,HomeWork
from teacher.forms import HomeWorkForm

# Create your views here.

def homeview(request):
    return render(request,"home.html")

class Homeview(View):
    def get(self,request):
        return render(request,"home.html")
    
class studentlistview(View):
    def get(self,request,*args,**kwargs):
        student_qs=Student.objects.all()
        return render(request,"studentlist.html",{"data":student_qs})
    
class AddStudentView(View):
    def get(self,request):
        return render(request,"addstudent.html")
    def post(self,request):
        name=request.POST.get('name')
        age=request.POST.get('age')
        batch=request.POST.get('batch')
        place=request.POST.get('place')
        Student.objects.create(name=name,age=age,batch=batch,place=place)
        return redirect('slist')
    
class EditStudentView(View):
    def get(self,request,**kwargs):
        student_id=kwargs.get('sid')
        student_obj=Student.objects.get(id=student_id)
        return render(request,"editstudent.html",{"student":student_obj})
    def post(self,request,**kwargs):
        name=request.POST.get('name')
        age=request.POST.get('age')
        batch=request.POST.get('batch')
        place=request.POST.get('place')
        student_obj=Student.objects.get(id=kwargs.get('sid'))
        student_obj.name=name
        student_obj.age=age
        student_obj.batch=batch
        student_obj.place=place
        student_obj.save()
        return redirect('slist') 


class DeleteStudentView(View):
    def get(self,request,*args,**kwargs):
        Student_id=kwargs.get('sid')
        Student.objects.get(id=Student_id).delete()
        return redirect('slist')
    
# Home Works

class HomeWorklistView(View):
    def get(self,request):
        hws=HomeWork.objects.all()
        return render(request,"homeworklist.html",{"data":hws})
    
class AddHomeworkView(View):
      def get(self,request):
        form=HomeWorkForm()
        return render(request,"addhomework.html",{"form":form})
      def post(self,request):
        # subject=request.POST.get('subject')
        # question=request.POST.get('question')
        # date=request.POST.get('submit_date')
        form_data=HomeWorkForm(data=request.POST)
        if form_data.is_valid():
            subject=form_data.cleaned_data.get('subject')
            question=form_data.cleaned_data.get('question')
            submit_date=form_data.cleaned_data.get('submit_date')
            HomeWork.objects.create(subject=subject,question=question,submit_date=submit_date)
            return redirect('hwlist')
        return HttpResponse("validation Failed")
      
class DeleteHwView(View):
    def get(self,request,**kwargs):
        hid = kwargs.get('hid')
        HomeWork.objects.get(id=hid).delete()
        return redirect('hwlist')
    
class EditHwView(View):
    def get(self,request,**kwargs):
        hid=kwargs.get('hid')
        hw=HomeWork.objects.get(id=hid)
        form=HomeWorkForm(initial={"subject":hw.subject,"question":hw.question,"submit_date":hw.submit_date})
        return render(request,"editHw.html",{"form":form})
    def post(self,request,**kwargs):
        hid=kwargs.get('hid')
        hw=HomeWork.objects.get(id=hid)
        form_data=HomeWorkForm(data=request.POST)
        if form_data.is_valid():
            subject=form_data.cleaned_data.get('subject')
            question=form_data.cleaned_data.get('question')
            submit_date=form_data.cleaned_data.get('submit_date')
            hw.subject=subject
            hw.question=question
            hw.submit_date=submit_date
            hw.save()
            return redirect('hwlist')
        return HttpResponse("Validation Failed")


    
     
    
# class AddTeacherView(View):
#     def get(self,request):
#         teachform=TeacherForm(
#         return render(request,"addteach.html",{"form":teachform})
#     def post(self,request):
#         form_data=TeacherForm(data=request.POST,files=request.FILES)
#         if form_data.is_valid():
#             form_data.save()
#             message.success(request,"Teacher Added!!")
#             return redirect('officehome')
#         messages.warning(request,"Adding Teacher Failed")
#         return render(request,"addteach.html",{"form":form_data})
    

# class TeacherListView(View):
#     def get(self,request):
#         teachlist=Teacher.objects.all()
#         return render(request,"teachlist.html",{"data":teachlist})
    
# class DeleteTeacherView(View):
#     def get(self,request,**kwargs):
#         tid=kwargs.get('id')
#         Teacher.objects.get(id=tid).delete()
#         return redirect('teacherlist')

# class EditTeachView(View):
#     def get(self,request,**kwargs):
#         tid=kwargs.get('id')
#         teach=Teacher.objects.get(id=tid)
#         form=TeacherForm(instance=teach)
#         return render(request,'editteach.html',{"form":form})
#     def post(self,request,**kwargs):
#         tid=kwargs.get('id')
#         teach=Teacher.objects.get(id=tid)
#         form_data=TeacherForm(data=request.POST,files=request.FILES,instance=teach)
#         if form_data.is_valid():
#             form_data.save()
#            messages.info(request,"Teacher data updated")
#         return render(request,"editTeach.html",{"form":form_data})


def clean(self):
    cleaned_data=super().clean()
    print(cleaned_data)
    age=cleaned_data.get('age')
    ph=cleaned_data.get('phone')
    if age<18:
        self.add_error('age',"age must be greater than 18")
    if len(ph)!=10:
        self.add_error('phone',"phone number must be 10 digits")
    return cleaned_data




