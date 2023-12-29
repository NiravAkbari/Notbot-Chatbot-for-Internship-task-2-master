# Generated by Django 4.2.5 on 2023-10-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('recipient', models.CharField(max_length=255)),
                ('scheduled_time', models.DateTimeField()),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]