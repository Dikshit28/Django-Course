from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, response,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string
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
    try:
        res=monthly_tasks[month]
        #res=render_to_string("challenges/challenge.html")
        '''3rd argument sent for dynamic rendering of HTML template'''
        return render(request,"challenges/challenge.html",{
            "text":res,
            "month":month
            })
    except:
        raise Http404()
    

def month_list(request):
    months= monthly_tasks.keys()
    return render(request,"challenges/index.html",
                    {
                        "months":months,
                    }
                )