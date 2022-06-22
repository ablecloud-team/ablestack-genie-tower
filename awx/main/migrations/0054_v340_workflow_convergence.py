# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_v340_workflow_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowjobnode',
            name='do_not_run',
            field=models.BooleanField(
                default=False,
                help_text='Indidcates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.',
            ),
        ),
    ]
