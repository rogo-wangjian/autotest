import datetime
from enum import Enum

from django.db import models


# Create your models here.


class TaskState(Enum):
    Unknown = 0

    Created = 10
    Running = 20
    Paused = 30

    Completed = 40
    Failed = 50
    Cancelled = 100

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)


class PackageState(Enum):
    Unknown = 0

    Created = 10  # 已创建 - 无货

    Collected = 100  # 已取货 - 有货
    Shipping = 110  # 配送中 - 有货
    Arrived = 120  # 待取货 - 有货
    OnHold = 190  # 暂存 (滞留 / 自提)  - 有货

    Success = 200  # 终态 | 已成功 - 无货
    Failed = 300  # 终态 | 已失败 (取消 / 异常) - 无货

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)


class TestTask(models.Model):

    # 循环次数
    loop_count = models.IntegerField(verbose_name="循环次数", default=1)
    # 任务参数
    request_params = models.JSONField(verbose_name="任务参数", default=dict)
    created_at = models.DateTimeField(
        default=datetime.datetime.now, verbose_name="创建时间"
    )


class TaskRecord(models.Model):
    unit_uid = models.IntegerField(verbose_name="设备Id")
    task_state = models.IntegerField(
        choices=TaskState.choices(),
        verbose_name="包裹状态",
        default=TaskState.Unknown.value,
    )
    package_state = models.IntegerField(
        max_length=16,
        choices=PackageState.choices(),
        verbose_name="任务状态",
        default=PackageState.Unknown.value,
    )
