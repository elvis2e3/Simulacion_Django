from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from sympy import latex,symbols,apart,together

# Create your views here.
def home(request):
    print "--->>>",request
    index=get_template('index.html')
    c=Context({'hola':"hola mundo"})
    html=index.render(c)
    return HttpResponse(html)

def calcular(request):
#    print dir(request)
    datos=request.GET
    print datos.get('lx')
    print datos.get('ly')
    res="<!DOCTYPE html><html><head><title>Lagrange</title><script type='text/javascript' src='/static/MathJax.js?config=TeX-AMS_HTML'></script></head><body><div ><hr>"
    xl=(datos.get('lx')).split(",")
    yl=(datos.get('ly')).split(",")
    for i in range(len(xl)):
        xl[i]=int(xl[i])
        yl[i]=int(yl[i])
    lagrange=0
    x = symbols('x')
    for j in range(len(yl)):
        lx=1
        for i in range(len(xl)):
            if j!=i:
                lx=lx*((x-xl[i])/(xl[j]-xl[i]))
        #lx=together(apart(lx,x),x)
        #res=res+latex(lx, mode='equation')+"<br>"
        #res=res+"<hr>"
        res=res+" multiplicando por "+str(yl[j])+"<br>"
        lx=lx*yl[j]
        lx=together(apart(lx,x),x)
        res=res+latex(lx, mode='equation')+"<br>"
        res=res+"<hr>"
        res=res+ "<br>"
        lagrange=lagrange+lx
    res=res+ "La funcion resultado es:<br>"
    lagrange=together(apart(lagrange,x),x)
    lista=[]
    for i in range(1,21):
        lista.append(lagrange.subs(x,i))
    res=res+latex(lagrange, mode='equation')+"<br>"
    res=res+"<div><canvas id='lineChart' height='140'></canvas></div></div><script src='/static/jquery-2.1.1.js'></script><script src='/static/chartJs/Chart.min.js'></script>"
    res=res+"""
            <script>$(function () {var lineData = {
                labels: ["1", "2", "3", "4", "5", "6", "7","8","9","10","11","12","13","14","15","16","17","18","19","20"],
                datasets: [{
                        label: "funcion",backgroundColor: 'rgba(26,179,148,0.5)',
                        borderColor: "rgba(26,179,148,0.7)",pointBackgroundColor: "rgba(26,179,148,1)",
                        pointBorderColor: "#fff",data: """+lista.__str__()+"""
                    }]};
            var lineOptions = {responsive: true};var ctx = document.getElementById("lineChart").getContext("2d");new Chart(ctx, {type: 'line', data: lineData, options:lineOptions});
        });</script>
    """
    res=res+"</body></html>"

    #return HttpResponseRedirect("/")
    return HttpResponse(res)