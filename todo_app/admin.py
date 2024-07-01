# 这里是用来注册django管理后台的，

from django.contrib import admin

# Register your models here.
# 从当前目录的models.py 文件中导入task模型，
from .models import Task


# 定义名为taskAdmin类，该类用来配置task模型在管理后台中显示的方式和操作方式
class TaskAdmin(admin.ModelAdmin):

    # 指定在管理后台的列表视图中，这里显示task is completed，updated at 字段
    list_display = ('task', 'is_completed', 'updated_at')

    # 哪些字段可以进行搜索，这里指定task字段可以进行搜索
    search_fields = ('task',)


# 将task模型注册到管理后台，并使用taskAdmin类来配置它的显示和操作方式
admin.site.register(Task, TaskAdmin)
