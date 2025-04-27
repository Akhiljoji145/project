from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie,Category
from add.models import Rating
from django.contrib.auth.models import User
from django.contrib.auth import logout
from movie.models import Movie,Category
from .forms import CustomUserCreationForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request):
	movie_list=Movie.objects.all().order_by('-relea_date')
	category=Category.objects.all()
	paginator=Paginator(movie_list,6)
	try:
		page=int(request.GET.get('page','1'))
	except:
		page=1
	try:
		movie=paginator.page(page)
	except (EmptyPage,InvalidPage):
		movie=paginator.page(paginator.num_pages)
	return render(request,'movielist.html',{'movie':movie,'category':category})

def login(request):
    return render(request, 'login.html')

def moviedetail(request,mov_id):
	movie=Movie.objects.get(id=mov_id)
	category = Category.objects.all()
	user=User.objects.all()
	try:
		rating=Rating.objects.all().filter(movie=mov_id).values()
		return render(request,'moviedetail.html',{'movie':movie,'rating':rating,'user':user,'category':category})
	except Rating.DoesNotExist:
		return render(request,'moviedetail.html',{'movie':movie,'user':user,'category':category})

def usermoviedetail(request,user_name,mov_id):
	movie=Movie.objects.get(id=mov_id)
	user=User.objects.get(id=user_name)
	category = Category.objects.all()
	try:
		rating=Rating.objects.all().filter(movie=mov_id).values()
		return render(request,'moviedetail.html',{'movie':movie,'user':user,'rating':rating,'category':category})
	except Rating.DoesNotExist:
		return render(request,'moviedetail.html',{'movie':movie,'user':user,'category':category})
def logout_view(request):
	logout(request)
	return redirect('/')

def user_home(request,user_id):
	movie=Movie.objects.all()
	user=User.objects.get(id=user_id)
	category = Category.objects.all()
	return render(request,'movielist.html',{'movie':movie,'user':user,'category':category})

def userlogin(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		passw = request.POST.get('pass')
		try:
			user = User.objects.get(username=name)
			movie=Movie.objects.all()
			category = Category.objects.all()
			if user.check_password(passw):
 				return render(request,'user_movielist.html',{'user':user,'movie':movie,'category':category})
			else:
				return render(request,'login.html')
		except User.DoesNotExist:
			return render(request, 'register.html')
	return render(request, 'login.html')

def user_reg(request):
	if request.method == 'POST':
		form =CustomUserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			return redirect('/login/')
	else:
		category = Category.objects.all()
		form=CustomUserCreationForm()
	return render(request,'register.html',{'form':form,'category':category})

def user_details(request, user_id):
	category = Category.objects.all()
	user = User.objects.get(id=user_id)
	return render(request,'user_details.html', {'user': user,'category':category})

def cat_movie(request,cat_name):
	category = Category.objects.all()
	mov=Movie.objects.filter(category=cat_name)
	return render(request,'category.html',{'mov':mov,'category':category})