# Generated by Django 3.1.7 on 2021-04-06 18:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sub_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(max_length=1000)),
                ('discount', models.IntegerField(default=0, max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rating', models.IntegerField(default=0, max_length=1)),
                ('qty', models.IntegerField(default=0, max_length=6)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_admin.category')),
            ],
        ),
    ]
