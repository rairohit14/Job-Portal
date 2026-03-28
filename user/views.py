from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm

# user login

from django.shortcuts import render, redirect

# user logout
from django.contrib.auth import logout

# dashboard page
from django.contrib.auth.decorators import login_required

# job post
from .models import Job
from .forms import JobForm
from django.contrib.auth.decorators import login_required

# view job list
from .models import Job

# Apply job feature
from.models import Apply

#Applied Jobs Page
from.models import Apply
from django.contrib.auth.decorators import login_required


def home(request):
    return redirect('/login/')
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
            
    return render(request, 'register.html', {'form': form})

# user login 

def user_login(request):
    if request.method == 'POST':
        from django.contrib.auth import authenticate, login

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'login.html')


# user log_out

def user_logout(request):
    logout(request)
    return redirect('/login/')

# dashboard page
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# job post
@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('/dashboard/')
    else:
        form = JobForm()

    return render(request, 'create_job.html', {'form': form})


# view job list
def job_list(request):
    jobs = Job.objects.all()

    for job in jobs:
        job.already_applied = Apply.objects.filter(user=request.user, job=job).exists()

    return render(request, 'job_list.html', {'jobs': jobs})

# Apply job feature

@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    Apply.objects.create(user=request.user, job=job)
    return redirect('/jobs/')

#Applied Jobs Page
@login_required
def applied_jobs(request):
    applied = Apply.objects.filter(user=request.user)
    return render(request, 'applied_jobs.html', {'applied': applied})

