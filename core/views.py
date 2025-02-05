from django.shortcuts import render, redirect
from .models import test, robot
from django.contrib import messages
# Create your views here.
def home(request):
    robots = robot.objects.all()

    if request.method == 'POST':
        message = request.POST['message']
        img = request.FILES.get('img')
        repeat = request.POST.get('repeat', 'off') == 'on'
        robot_id = request.POST['robot']
        time = request.POST['time']
        timeframe = request.POST['timeframe']

        selected_robot = robot.objects.get(id=robot_id) if robot_id else None

        test.objects.create(
                    message=message, img=img, repeat=repeat, robot=selected_robot, time=time, timeframe=timeframe
                )
        
        return redirect('core:dashboard')
        

    return render(request, 'home.html', {'robots': robots})

def dashboard(request):
    tasks = test.objects.all()
    return render(request, 'dashboard.html', {'tasks': tasks})

def bot_dashboard(request):
    bot = robot.objects.all()

    return render(request, 'bot_dashboard.html',{'bots':bot})

def add_bot(request):
    if request.method == 'POST':
        robot_name = request.POST['name']
        organization_name = request.POST['organization']
        robot_key = request.POST['key']

        robot.objects.create(
            robot_name=robot_name, organization_name=organization_name, robot_key=robot_key
        )
        messages.success(request,'Bot added sucessfully')
        return redirect('core:bot_dashboard')

    return render(request, 'add_bot.html')


def edit_task(request, task_id):
    task = test.objects.get(id=task_id)
    robots = robot.objects.all().exclude(id=task.robot_id)

    if request.method == 'POST':
        task.message = request.POST['message']
        task.time = request.POST['time']
        if request.POST.get('altered_image', 'off') == 'on':
            task.img = request.FILES.get('img')
        task.repeat = request.POST.get('repeat', 'off') == 'on'
        task.timeframe = request.POST['timeframe']
        task.robot = robot.objects.get(id=request.POST['robot'])
        task.save()
        return redirect('core:dashboard')

    return render(request, 'edit_task.html', {'task': task, 'robots': robots})

def edit_bot(request, bot_id):
    bot = robot.objects.get(id=bot_id)
    if request.method == 'POST':
        bot.robot_name = request.POST['name']
        bot.organization_name = request.POST['organization']
        bot.robot_key = request.POST['key']
        bot.save()
        return redirect('core:bot_dashboard')
    return render(request, 'edit_bot.html', {'bot': bot})

def delete_task(request, task_id):
    record = test.objects.get(id=task_id)
    record.delete()

    return redirect('core:dashboard')

def delete_bot(request, bot_id):
    record = robot.objects.get(id=bot_id)
    record.delete()

    return redirect('core:bot_dashboard')

