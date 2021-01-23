from django.shortcuts import render
# importing models.py so we can acess the data that we created in our database using queries instead of this dummy data
from .models import Post
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Conatct1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'

    },

    {
        'author': 'PriyankaER',
        'title': 'Contact123',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'


    }


]



def home(request):
    context = {
       'posts' : #  posts
                 Post.objects.all()

    }
    return render(request, 'contactbook/home.html', context)

def about(request):
    return render(request, 'contactbook/about.html',{'title':'About'})


