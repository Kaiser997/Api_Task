# Generated by Django 4.2 on 2024-07-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('ALTA', 'ALTA'), ('MEDIA', 'MEDIA'), ('BAJA', 'BAJA')], max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('BACKLOG', 'BACKLOG'), ('TODO', 'TODO'), ('DOING', 'DOING'), ('TEST', 'TEST'), ('DONE', 'DONE')], max_length=200),
        ),
    ]