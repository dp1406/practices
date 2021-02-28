from django.shortcuts import render

# Create your views here.
def session_page(requst):
    count=requst.session.get('count',0)
    newcount=count+1
    requst.session['count']=newcount
    return render(requst,'testapp/count.html',{"count":newcount})
