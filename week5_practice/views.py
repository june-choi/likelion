from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    teamnumber = int(request.GET["teamnumber"])

    if teamnumber == 4: 
        result = "멋장이 사조조"
    else:
        result = "다른 번호를 입력해봐!"

    return render(request, 'result.html', {"result": result})
