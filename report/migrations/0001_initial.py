# Generated by Django 4.1 on 2022-08-23 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=255)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InComeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_income', models.CharField(max_length=255)),
                ('month_customer', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='report.reportmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.CharField(max_length=255)),
                ('advertising', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('report_expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_expense', to='report.reportmodel')),
            ],
        ),
    ]
