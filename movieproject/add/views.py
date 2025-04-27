from django.shortcuts import render,redirect,get_object_or_404
from movie.models import Movie,Category
from django.contrib.auth.models import User
from .forms import UpdateMovieForm,ProfileForm
from .models import Rating
# Create your views here.
def addmovie(request, user_id):
    user = get_object_or_404(User, id=user_id)
    categories = Category.objects.all()
    movie=Movie.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('img')
        trailer = request.POST.get('trailer')
        banner = request.FILES.get('banner')
        desc = request.POST.get('desc')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id)  # Get the Category instance
        date = request.POST.get('date')

        movies = Movie(name=name, image=image, trailer=trailer, banner=banner, desc=desc, category=category, relea_date=date, user=user.username)
        movies.save()
        return render(request,'user_movielist.html',{'user':user,'movie':movie})
    return render(request, 'add_movie.html',{'user':user,'category': categories})
def deletemovie(request,mov_id,user_id):
	movies=Movie.objects.get(id=mov_id)
	user=User.objects.get(id=user_id)
	movie=Movie.objects.all()
	movies.delete()
	return render(request,'user_movielist.html',{'movie':movie,'user':user})
def update(request,mov_id,user_id):
	movies=Movie.objects.get(id=mov_id)
	user=User.objects.get(id=user_id)
	movie=Movie.objects.all()
	form=UpdateMovieForm(request.POST or None,request.FILES,instance=movies)
	if form.is_valid():
		form.save()
		return render(request,'user_movielist.html',{'movie':movie,'user':user})
	return render(request,'update.html',{'movies':movies,'user':user,'form':form})

def rate(request,mov_id,user_id):
    users=User.objects.get(id=user_id)
    movies=Movie.objects.get(id=mov_id)
    ratings=Rating.objects.all().filter(movie=mov_id)
    if request.method=='POST':
        rate=request.POST.get('rate')
        review=request.POST.get('review')
        movie_id=request.POST.get('movie_id')
        user=request.POST.get('user')
        try:
            rating=Rating(rating=rate,review=review,movie=movie_id,user=user)
            rating.save()
        except Rating.DoesNotExist:
            return render(request,'moviedetail.html',{'movie':movies,'user':users})
    return render(request,'moviedetail.html',{'movie':movies,'user':users,'rating':ratings})



def UpdateUser(request,user_id):
	user=User.objects.get(id=user_id)
	form=ProfileForm(request.POST or None,request.FILES,instance=user)
	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request,'update.html',{'user':user,'form':form})

def delete_rate(request,mov_id,user_id,rate_id):
    users=User.objects.get(id=user_id)
    movies=Movie.objects.get(id=mov_id)
    ratings=Rating.objects.all().filter(movie=mov_id)
    rated=Rating.objects.get(id=rate_id)
    rated.delete()
    return render(request,'moviedetail.html',{'movie':movies,'user':users,'rating':ratings})


