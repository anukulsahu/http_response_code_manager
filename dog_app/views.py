from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
import re

# Create your views here.
def logout_page(request):
  logout(request)
  return redirect('/login')

def login_page(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username=username).exists():
      messages.error(request,"Invalid Credentials!")
      return redirect('/login')
    user = authenticate(username=username,password=password)
    if user is None:
      messages.error(request,"Invalid Credentials!")
      return redirect('/login')
    else:
      login(request,user)
      return redirect('/search') 
  return render(request,"login_page.html")

def signup_page(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if first_name=='' or last_name=='' or username=='' or password=='':
      messages.error(request, "All fields are required!")
      return redirect('/signup')
    user = User.objects.filter(username=username)
    if user.exists():
      messages.info(request,"Username already taken, try different username")
      return redirect('/signup')
    
    user = User.objects.create(
      first_name = first_name,
      last_name = last_name,
      username = username
    )
    user.set_password(password)
    user.save()
    messages.info(request,"Account created successfully!")
  return render(request,"signup_page.html")
@login_required(login_url="/login")
def search_page(request):
  filter_input = request.GET.get('filter','')
  http_status_codes = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 218, 226, 300, 301, 302, 303, 304, 305, 306,307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 428, 429, 430, 431, 440, 444, 449, 450, 451, 460, 463, 464, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 520, 521, 522, 523, 524, 525, 526, 527, 529, 530, 561, 598, 599, 999]
  
  images_dict = {}
  if filter_input !='':
    pattern = filter_input.replace('x',r'\d')
    code_list = []
    for code in http_status_codes:
      if re.match(pattern,str(code)):
        code_list.append(code)
      
    for code in code_list:
      images_dict[code] = f"https://http.dog/{code}.jpg"

  if request.method == "POST":
    list_name = request.POST.get('list_name')
    response_codes = ','.join(map(str, images_dict.keys()))
    image_links = ','.join(images_dict.values())
    
    ResponseCodeModel.objects.create(
      user = request.user,
      name = list_name,
      response_codes = response_codes,
      image_links = image_links,
    )
    return redirect('/list')
    

  return render(request,"search_page.html",{'images':images_dict})

@login_required(login_url="/login")
def list_page(request):
  user_list = ResponseCodeModel.objects.filter(user = request.user)
  # print(user_list)
  if request.method == "POST":
    delete_list_id = request.POST.get('delete_list_id')
    list_to_delete = ResponseCodeModel.objects.filter(id=delete_list_id, user = request.user)
    list_to_delete.delete()
  return render(request,"list_page.html",{'user_list':user_list})

@login_required(login_url="/login")
def view_list(request,id):
  saved_list = ResponseCodeModel.objects.filter(id = id, user = request.user)
  list_name=saved_list[0].name
  creation_date=saved_list[0].creation_date

  images_dict={}   #dictionary for storing(code,link)
  response_codes = saved_list[0].response_codes.split(',') #converting to list
  image_links = saved_list[0].image_links.split(',')  #converting to list
  
  for i in range(len(response_codes)):
    images_dict[response_codes[i]] = image_links[i]
  print(images_dict)
  return render(request, "view_list.html", {'list_name':list_name,'creation_date':creation_date, 'images_dict':images_dict})