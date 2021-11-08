# Generated by Django 3.2.6 on 2021-10-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grabezy_app', '0007_rename_isssue_contact_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.TextField(max_length=50000)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=12)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(default='', max_length=6)),
                ('state', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]