from django.urls import path
from . import views

# 定义列表，用来存放url模式
# addTask是url相对路径，表示访问 http://127.0.0.1:800/addTask/ 会触发相应的视图函数
# views.addTask 指定了当访问这个url时，将调用views.py文件中的addTask函数，
# 以下都是同理
urlpatterns = [
    # addtask
    path('addTask/', views.add_task, name='add_task'),

    # markdone
    path('mark_as_down/<int:pk>', views.mark_as_done, name='mark_as_done'),

    # mark undone
    path('mark_as_unDone/<int:pk>', views.mark_as_undone, name="mark_as_unDone"),

    # edit task
    path('edit_task/<int:pk>', views.edit_task, name="edit_task"),

    # delete task
    path('delete_task/<int:pk>', views.delete_task, name="delete_task"),
]