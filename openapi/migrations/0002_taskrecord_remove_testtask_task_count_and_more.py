# Generated by Django 4.0.1 on 2022-01-10 12:46

import datetime
from django.db import migrations, models
import openapi.models


class Migration(migrations.Migration):

    dependencies = [
        ("openapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unit_uid", models.IntegerField(verbose_name="设备Id")),
                (
                    "task_state",
                    models.CharField(
                        choices=[
                            ("Unknown", 0),
                            ("Created", 10),
                            ("Running", 20),
                            ("Paused", 30),
                            ("Completed", 40),
                            ("Failed", 50),
                            ("Cancelled", 100),
                        ],
                        default=openapi.models.TaskState["Unknown"],
                        max_length=16,
                        verbose_name="包裹状态",
                    ),
                ),
                (
                    "package_state",
                    models.CharField(
                        choices=[
                            ("Unknown", 0),
                            ("Created", 10),
                            ("Collected", 100),
                            ("Shipping", 110),
                            ("Arrived", 120),
                            ("OnHold", 190),
                            ("Success", 200),
                            ("Failed", 300),
                        ],
                        default=openapi.models.PackageState["Unknown"],
                        max_length=16,
                        verbose_name="任务状态",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="testtask",
            name="task_count",
        ),
        migrations.AddField(
            model_name="testtask",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="创建时间"
            ),
        ),
        migrations.AddField(
            model_name="testtask",
            name="request_params",
            field=models.JSONField(default="", verbose_name="任务参数"),
        ),
        migrations.AlterField(
            model_name="testtask",
            name="loop_count",
            field=models.IntegerField(default=1, verbose_name="循环次数"),
        ),
    ]
