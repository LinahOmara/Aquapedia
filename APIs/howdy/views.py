# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import subprocess
import json
# Create your views here.
class Latest_bill(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt") as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Bill":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class History(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "History":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class Expected_bill(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Expected bill":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)


class Bill_date(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Due to":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class Actualtillnow(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Actual till now":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class ActualVsExpected(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Actual Vs Expected":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class Tier(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Current tier":
                    return JsonResponse({'tier' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'tier' : 'not found'} , safe = False)

class TierUpdates(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Tier Updates":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)
class Msg(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "msg":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class Leakage(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Leakage updates":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)
class LastUpdate(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Updated at":
                    return JsonResponse({'test' : var} , safe = False)
                else:
                    continue
        return JsonResponse({'test' : 'not found'} , safe = False)

class Comparison(TemplateView):
    def get(self, request, **kwargs):
        Matrix = [0 for x in range(3)]
        with open("/home/aya/Desktop/Aquapedia/Reports/"+ request.GET.urlencode()[:-1] +".txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "You":
                    Matrix[0] = var
                if name == "Neighbours":
                    Matrix[1] = var
                if name == "Efficient Neighbours":
                    Matrix[2] = var
                else:
                    continue
        print (Matrix[0])
        return JsonResponse({'test' : Matrix}  , safe = False)

####################Company APIs###############################################################
 # GET number of users
class UsersCount(TemplateView):
    def get(self, request, **kwargs):
        response = {'users':'43'}
        return JsonResponse(response, safe = False)

 # GET abnormal behaviours of users
class Alterts(TemplateView):
     def get(self, request, **kwargs):
        response = [
        {'user_id':'5' , 'alerts':'Leakage'},
        {'user_id':'54', 'alerts':'Leakage'},
        {'user_id':'23', 'alerts':'Sudden stop'}]
        # response = {'test' : '100'}
        return JsonResponse(response, safe = False)        

class Geographic(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/company.txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Statistics":
                    data = json.loads(var)
                    return JsonResponse(data, safe = False)
                else:
                    continue
        return JsonResponse(response, safe = False)

class Predict(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/company.txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Predictions":
                    data = json.loads(var)
                    return JsonResponse(data, safe = False)
                else:
                    continue
        return JsonResponse(response, safe = False)

class Analysis(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/aya/Desktop/Aquapedia/Reports/company.txt")  as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                if name == "Analysis":
                    data = json.loads(var)
                    return JsonResponse(data, safe = False)
                else:
                    continue
        return JsonResponse(response, safe = False)
