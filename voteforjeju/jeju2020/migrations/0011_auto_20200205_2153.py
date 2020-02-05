# Generated by Django 2.2.7 on 2020-02-05 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jeju2020', '0010_auto_20200205_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='promise',
            name='text10',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='promise',
            name='text11',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='promise',
            name='text6',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='promise',
            name='text7',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='promise',
            name='text8',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='promise',
            name='text9',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='press',
            name='candidate',
            field=models.ForeignKey(default='hi', on_delete=django.db.models.deletion.CASCADE, to='jeju2020.Candidate'),
        ),
        migrations.AlterField(
            model_name='promise',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jeju2020.Candidate'),
        ),
    ]
