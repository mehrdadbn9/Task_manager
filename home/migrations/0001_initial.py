# Generated by Django 3.1.7 on 2021-02-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=1)),
            ],
        ),
    ]
