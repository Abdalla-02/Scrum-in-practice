# Generated by Django 5.0.2 on 2024-02-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_name_tree_gattung_tree_pflanzjahr'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='gebiet',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tree',
            name='strasse',
            field=models.CharField(default='1', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tree',
            name='pflanzjahr',
            field=models.IntegerField(),
        ),
    ]