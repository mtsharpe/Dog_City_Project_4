# Generated by Django 2.0.5 on 2018-05-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogcity', '0006_auto_20180529_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('day', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='playdate',
            name='dogs',
        ),
        migrations.AddField(
            model_name='dog',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='owner',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Playdate',
        ),
        migrations.AddField(
            model_name='walk',
            name='dogs',
            field=models.ManyToManyField(to='dogcity.Dog'),
        ),
    ]
