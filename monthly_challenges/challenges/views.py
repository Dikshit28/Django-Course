from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, response,HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string
# Create your views here.

monthly_tasks={
    "jan":"JAN",
    "feb":"FEB",
    "mar":"MAR",
    "apr":"APR",
    "may":"MAY",
    "jun":"JUN",
    "jul":"JUL",
    "aug":"AUG",
    "sep":"SEP",
    "oct":"OCT",
    "nov":"NOV",
    "dec":"DEC"
}

def intindex(request,month):
    if month>len(monthly_tasks) or month<1:
        return HttpResponseNotFound("INVALID MONTH")
    res=list(monthly_tasks.keys())[month-1]
    response_url=reverse("monthly-challenges",args=[res])
    return HttpResponseRedirect(response_url)

def index(request,month):
    res=None
    if month in monthly_tasks.keys():
        res=monthly_tasks[month]
        #res=render_to_string("challenges/challenge.html")
        '''3rd argument sent for dynamic rendering of HTML template'''
        return render(request,"challenges/challenge.html",{
            "text":res,
            "month":month.capitalize()
            })
    else:
        return HttpResponseNotFound("Not in the list")
    

def month_list(request):
    res_str=""
    for i in list(monthly_tasks.keys()):
        month_url=reverse("monthly-challenges",args=[i])
        res_str+=f"<li><a href='{month_url}'>{i}</a></li>"
    res_data=f"<h1><ol>{res_str}</ol></h1>"
    return HttpResponse(res_data)