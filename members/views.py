from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.

def index(request):
    return HttpResponse("<h1>hello</h1>")

def test(request):
    return HttpResponse("<h2>test</h2>")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        member = Members(
                username = username,
                useremail = email
        )

        member.save()
        res_data = {}
        res_data['res'] = '등록성공'

        return render(request, 'index.html', res_data)

    return render(request, 'index.html')

def git(request):
    return HttpResponse("<h2>git version</h2>")

def gu(request):
    num = request.GET.get('num','')

    return HttpResponse(f'<h1> gugu : {num_gugu(num)} </h1>')

def num_gugu(num):

    st = ""
    for i in range(1,10):
        st += f"{num} * {i} = {int(num) * i}<br>"
     
    return st