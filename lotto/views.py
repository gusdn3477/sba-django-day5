from django.shortcuts import render
from django.http.response import HttpResponse
import random

# Create your views here.
def index(request):

    if request.method == 'GET':
        lotto = []

        while len(lotto) < 6:
            lotto.append(random.randint(1,46))
            lotto = list(set(lotto))
        return HttpResponse(f"<h1> 당신의 행운을 기원합니다</h1><br><h1>lotto 번호 추천 {lotto} </h1>")

    return HttpResponse("post")