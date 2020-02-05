# Generated by Django 2.2.7 on 2020-02-05 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jeju2020', '0017_auto_20200205_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='press',
            name='candidate',
            field=models.ForeignKey(default='hi', on_delete=django.db.models.deletion.CASCADE, to='jeju2020.Candidate'),
        ),
        migrations.AlterField(
            model_name='press',
            name='when',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='promise',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jeju2020.Candidate'),
        ),
    ]
