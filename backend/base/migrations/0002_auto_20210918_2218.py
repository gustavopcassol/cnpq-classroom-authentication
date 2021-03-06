# Generated by Django 3.0.14 on 2021-09-19 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("registered", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="courses", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.GenericIPAddressField()),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="positions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "get_latest_by": "created",
            },
        ),
        migrations.CreateModel(
            name="Lecture",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weekday",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ]
                    ),
                ),
                ("start", models.TimeField()),
                ("duration", models.DurationField()),
                (
                    "attendances",
                    models.ManyToManyField(
                        related_name="attendances",
                        through="base.Attendance",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="lectures",
                        to="base.Course",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="attendance",
            name="lecture",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="base.Lecture"
            ),
        ),
        migrations.AddField(
            model_name="attendance",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddConstraint(
            model_name="lecture",
            constraint=models.UniqueConstraint(
                fields=("course", "weekday"), name="unique_course_lecture_per_weekday"
            ),
        ),
    ]
