# Generated by Django 4.2.7 on 2023-12-06 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_delete_survey_alter_citizendetails_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizendetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='citizendetails',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]