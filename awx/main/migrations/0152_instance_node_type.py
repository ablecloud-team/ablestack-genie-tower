# Generated by Django 2.2.20 on 2021-07-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0151_rename_managed_by_tower'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='node_type',
            field=models.CharField(
                choices=[('control', 'Control plane node'), ('execution', 'Execution plane node'), ('hybrid', 'Controller and execution')],
                default='hybrid',
                max_length=16,
            ),
        ),
    ]
