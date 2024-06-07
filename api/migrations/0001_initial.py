# Generated by Django 4.2.13 on 2024-06-07 11:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(default='PENDING', max_length=20)),
                ('result', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
