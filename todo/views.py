from django.shortcuts import render
from todo_app.models import Task


# 定义home函数，接收request对象作为参数，该对象包含了用户的请求信息
# request对象是连接用户请求和django试图函数的桥梁，它包含了所有关于用户请求的信息，方便你在视图函数中进行处理
def home(request):

    query = request.GET.get('query', '')

    if query:
        tasks = Task.objects.filter(task__icontains=query, is_completed=False).order_by('-updated_at')
        completed_tasks = Task.objects.filter(task__icontains=query, is_completed=True).order_by('-updated_at')

    else:
        # 获取task模型的所有对象，表示所有的待办事项
        # 并筛选中is completed为false的待办事项，表示未完成的待办事项
        # 将未完成的待办事项按update at字段降序排列，最新的待办事项排在最前面
        tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

        # 与上一行类似，不过这里是筛选出is completed为false的待办事项，表示已经完成的待办事项
        completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

        # 将未完成和已完成的待办事项存储在名为context字典中
        # 这个字典将被传递给模版，已便模版使用这些数据渲染画面
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'query': query,  # 保留用户搜索的内容
    }

    # 使用render函数渲染home html模版，
    # request对象用来获取用户请求的信息
    # context字典用来将数据传递给模版
    # 最后 返回渲染后的html页面给用户
    return render(request, 'home.html', context)
