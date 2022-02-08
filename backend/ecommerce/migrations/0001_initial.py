# Generated by Django 4.0.2 on 2022-02-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('countInStock', models.IntegerField(default=0)),
                ('short_description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('long_description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
