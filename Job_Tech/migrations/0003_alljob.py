# Generated by Django 4.1.4 on 2022-12-28 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Tech', '0002_hr'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('desc', models.TextField()),
                ('company', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=30)),
                ('hr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Job_Tech.hr')),
            ],
        ),
    ]