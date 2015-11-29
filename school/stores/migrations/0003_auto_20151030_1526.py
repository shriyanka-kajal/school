# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields
from django.conf import settings
import common.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0002_auto_20151025_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add1', models.CharField(max_length=50)),
                ('add2', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(default=b'India', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CartList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.ForeignKey(related_name='stores_cartlist_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.ForeignKey(related_name='stores_category_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=20)),
                ('colorcode', colorful.fields.RGBColorField(default=b'#FFFFFF')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.ForeignKey(related_name='stores_images_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('rating', common.models.RangeField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('review', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user']},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subscribed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='creator',
            field=models.ForeignKey(related_name='stores_userprofile_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='product',
            field=models.ForeignKey(to='stores.Product'),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='pincode',
            field=models.ForeignKey(to='stores.Pincode'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address_fk',
            field=models.ForeignKey(blank=True, to='stores.Address', max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='ratings',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='cartlist',
            unique_together=set([('user', 'product')]),
        ),
    ]
