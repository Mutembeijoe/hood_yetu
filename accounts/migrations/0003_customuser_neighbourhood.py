# Generated by Django 2.2.7 on 2019-11-28 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0001_initial'),
        ('accounts', '0002_auto_20191128_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='neighbourhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='residents', to='neighbourhood.Neighbourhood'),
        ),
    ]
