from django.http import response
from django.shortcuts import redirect, render
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Stud
from rest_framework.decorators import api_view
from .serializers import seruser


# Create your views here.
@api_view(['POST', 'GET'])
def test(request):
    dataa = Stud.objects.all()
    if request.method == 'POST':
        if 'editt' in request.data:
            print('edit action detected')
            persentFromButton = request.data.get('editt')
            print(persentFromButton)
            oldRate = Stud.objects.get(id=persentFromButton)
            newrata = seruser(instance=oldRate, data=request.data)
            if newrata.is_valid():
                newrata.save()  # هنا يتم الحفظ إذا كانت البيانات صالحة
                return redirect('http://127.0.0.1:8000/one/aaa/')
            else:
                return Response(newrata.errors, status=400)
            

        if 'delete' in request.POST:
            req = request.POST.get('iid')
            try:
                cho = Stud.objects.get(id=req)
                cho.delete()
                return redirect('http://127.0.0.1:8000/one/aaa/')
            except Stud.DoesNotExist:
                return HttpResponse('items not found', status= status.HTTP_404_NOT_FOUND)
        
        if 'addd' in request.POST:
            add=seruser(data = request.POST)
            if add.is_valid():
                add.save()
                return redirect('http://127.0.0.1:8000/one/aaa/')
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


    return render(request, 'index.html',{'st':dataa, 'tass':Stud})


# def Upd(request):
    
#     
#     dataa = Stud.objects.all()
#     if request.method == 'POST':
        
#     return render(request, 'index.html',{'st':dataa})



def confDel(request):
        task = Stud.objects.get(id=pk)
        if request.method == 'POST':
            if 'yess' in request.POST:
                task.delete()
                print('requestPOSt')
                return redirect('http://127.0.0.1:8000/one/test/')
            if 'noo' in request.POST:
                return redirect('http://127.0.0.1:8000/one/test/')
        
        return render(request, 'del.html', {})

def upd (request, pk):
    stt = Stud.objects.get(id = pk)