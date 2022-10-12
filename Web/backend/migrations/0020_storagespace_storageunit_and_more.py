# Generated by Django 4.1.1 on 2022-10-04 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_rename_group_groupinfo_alter_userinfo_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='StorageSpace',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('orderpoint', models.PositiveSmallIntegerField(default=0)),
                ('standard_order_amount', models.PositiveSmallIntegerField(default=0)),
                ('maximal_capacity', models.PositiveSmallIntegerField(default=0)),
                ('amount', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StorageUnit',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('building', models.CharField(max_length=30)),
                ('floor', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='storagecomponent',
            name='article',
        ),
        migrations.RemoveField(
            model_name='storagecomponent',
            name='storage',
        ),
        migrations.RemoveField(
            model_name='article',
            name='alternative_articles',
        ),
        migrations.RemoveField(
            model_name='article',
            name='alternative_names',
        ),
        migrations.RemoveField(
            model_name='article',
            name='minimal_order_qt',
        ),
        migrations.RemoveField(
            model_name='article',
            name='refill_unit',
        ),
        migrations.RemoveField(
            model_name='article',
            name='std_cost',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sup_ordernr',
        ),
        migrations.RemoveField(
            model_name='article',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='article',
            name='take_out_unit',
        ),
        migrations.AddField(
            model_name='article',
            name='sanitation_level',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.DeleteModel(
            name='Storage',
        ),
        migrations.DeleteModel(
            name='storageComponent',
        ),
        migrations.AddField(
            model_name='storagespace',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article'),
        ),
        migrations.AddField(
            model_name='storagespace',
            name='storage_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.storageunit'),
        ),
    ]