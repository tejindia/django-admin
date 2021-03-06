# Generated by Django 3.1.7 on 2021-04-08 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub_admin', '0004_auto_20210407_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images/products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_admin.product')),
            ],
        ),
    ]
