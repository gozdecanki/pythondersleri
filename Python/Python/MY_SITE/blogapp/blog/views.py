from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog

data= {
    "blogs":[
        {
            "id": 1,
            "title":"Komple Uygulamalı Web Geliştirme Eğitimi 2026",
            "image": "1.png",
            "is_active": True,
            "is_home": False,
            "description":"Sıfırdan ileri seviyeye Fullstack Web Geliştirme: HTML, CSS, Bootstrap, JavaScript, React, ASP.NET Core ve API"

        },
         {
            "id": 2,
            "title":"Python Django ile RESTful API Geliştirme 2026",
            "image": "2.png",
            "is_active": True,
            "is_home": True,
            "description":"Django REST Framework ve JWT ile güvenli, ölçeklenebilir e-ticaret API’si kurun; ürün, sepet, sipariş ve kullanıcı yönet"

        },
         {
            "id": 3,
            "title":"Tailwind CSS 2026: Uygulamalı Projelerle Web Siteni Tasarla",
            "image": "3.png",
            "is_active": True,
            "is_home": True,
            "description":"Tailwind CSS’i en temelden öğrenin, modern ve mobil uyumlu arayüzler oluşturun. Projelerle konuları pekiştirin."

        },
         {
            "id": 4,
            "title":".NET & React ile FullStack E-Ticaret Projesi Geliştirme 2026",
            "image": "4.png",
            "is_active": False,
            "is_home": True,
            "description":"Asp.Net Core, React.js, Material UI ve Typescript kullanarak full-stack bir ticaret projesi geliştiriyoruz."

        }
    ]
}

# Create your views here.
def index (request):
    #return HttpResponse("home page")
    # context={
    #     "blogs": data["blogs"]
    # }
    #sqlite den gelen
    context={
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request,"blog/index.html", context)


def blogs (request):
    #return HttpResponse("blogs")
    # context={
    #     "blogs": data["blogs"]
    # }
    context={
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request,"blog/blogs.html", context)


def blog_details (request, id):
    #return HttpResponse("blog details " + str(id))
    #1. yöntem
    # blogs =data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    #2. yöntem comprehension
    # blogs =data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"]==id ][0]

    blog = Blog.objects.get(id=id)

    return render(request,"blog/blog-details.html",{
        "blog": blog
    })