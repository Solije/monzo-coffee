# Generated by Django 2.1.2 on 2018-10-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20181004_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('label', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('expression', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('activated', models.DateTimeField(auto_now_add=True, verbose_name='date activated')),
                ('tags', models.ManyToManyField(to='hello.Tag')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]