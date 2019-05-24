from django.shortcuts import render
from .models import FWS_DB_Helper
# Create your views here.
def index(req):
    return render(req, 'mainapp/index.html',{})

def loginPage(req):
    return render(req, 'mainapp/login.html',{})
def login(req):
    db = FWS_DB_Helper()
    cId = req.POST['cId']
    psw = req.POST['psw']
    user=db.getUser(cId)
    if user and user['psw']==psw:
        return render(req,'mainapp/debug.html',{'user':user})
    err="incorrect cId or password"
    return render(req, 'mainapp/debug.html', {'err': err})


def registerPage(req):

    return render(req, 'mainapp/register.html',{})

def register(req):
    name = req.POST['name']
    cId = req.POST['cId']
    dsgn = req.POST['dsgn']
    branch = req.POST['branch']
    email = req.POST['email']
    psw = req.POST['psw']
    db = FWS_DB_Helper()
    db.addUser({'name': name, 'cId': cId, 'dsgn': dsgn, 'branch': branch, 'email': email, 'psw': psw, 'tasks': [], 'subs': []})
    return render(req, 'mainapp/login.html',{})

def profile(req):
    return render(req, 'mainapp/profile.html',{})

def usersList(req):
    return render(req, 'mainapp/usersList.html',{})