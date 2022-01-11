from app_open_api_sdk import create_task
from app_open_api_sdk.codec import CreateTaskRequest
from django.contrib import admin

# Register your models here.
from openapi.models import TestTask, TaskRecord


@admin.action(description="创建任务")
def do_test(modeladmin, request, queryset):
    print(type(modeladmin), type(request), type(queryset))
    for q in queryset:
        q: TestTask
        create_task(request=CreateTaskRequest(**q.request_params))


class TestTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "loop_count", "created_at")
    actions = [do_test]


class TaskRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "unit_uid", "package_state", "task_state")


admin.site.register(TestTask, TestTaskAdmin)
admin.site.register(TaskRecord, TaskRecordAdmin)


admin.AdminSite.site_header = "YOGO自动化测试平台"
admin.AdminSite.site_title = "YOGO自动化测试平台"
