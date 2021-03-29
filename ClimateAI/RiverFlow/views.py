#Django Libs
from django.shortcuts import render
#Models
from RiverFlow.models import FlowData

from RiverFlow.Scripts.Functions import *




# Create your views here.

def Home(request):
    return render (request , 'App/Home.html')
    
def Predict(request):
    DatePred = request.POST.get('DatePred','')
    TableResult = Predict_NextDay(DatePred = DatePred)
    args = {'Table':TableResult}
    return render (request , 'App/Return/ReturnPredict.html',args)

def showGraph(request):
    Table = show_graphs()
    args={'Scatter':Table}
    return render (request , 'App/Graphs.html',args)
