from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.


# 添加待办事项函数
def add_task(request):

    # 获取用户输入的任务内容
    task = request.POST['task']

    # 创建新任务对象，并将任务内容保存到数据库中
    Task.objects.create(task=task)

    # 使用redirect重定向到主页
    return redirect('home')


# 将未完成的待办事项变更为已完成，也就是is completed变为True
def mark_as_done(request, pk):

    # 使用404获取指定ID的任务对象，
    task = get_object_or_404(Task, pk=pk)

    # 将任务对象is completed改为true
    task.is_completed = True

    # 使用task.save()保存更改到数据库
    task.save()

    # 重定向到主页
    return redirect('home')


# 将已完成的待办事项变更为未完成，也就是is completed变为False
def mark_as_undone(request, pk):

    # 使用404获取指定ID的任务对象，
    task = get_object_or_404(Task, pk=pk)

    # 将任务对象is completed改为False
    task.is_completed = False

    # 使用task.save()保存更改到数据库
    task.save()

    # 重定向到主页
    return redirect('home')


def edit_task(request, pk):

    # 使用404获取指定ID的任务对象，
    get_task = get_object_or_404(Task, pk=pk)

    # 有两种情况，用户点edit按钮编辑了task，用户点edit按钮没有编辑task
    # 这里需要做一个判断 如果用户编辑修改了task，则更新数据库的内容

    # 判断如果是post
    if request.method == 'POST':

        # 获取新的task
        new_task = request.POST['task']

        # 将获取到的被修改task更改为新的task
        get_task.task = new_task

        # 将更改保存到数据库
        get_task.save()

        # 重定向到主页
        return redirect('home')

    # 如果不是post，则将原数据重新渲染到当前页面
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)


# 删除task
def delete_task(request, pk):

    # 通过404获取指定id的对象
    task = get_object_or_404(Task, pk=pk)

    # 删除指定对象
    task.delete()

    # 重定向到主页
    return redirect('home')