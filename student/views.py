from django.shortcuts import render

# Create your views here.


  
def home(request):
   return render(request,'input.html')
  
def python(request):
  name1 = 'riya'
  name2 = 'john'
  name3 ='alex' 
  course1=request.GET["course"]
  if course1 == 'python':
    a = name1
  elif course1 == 'java':
    a = name2
  elif course1 == 'R':
    a = name3
  else :
    return 'none'
  return render(request,'output.html',{'b':a})


  