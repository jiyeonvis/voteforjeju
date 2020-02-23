# Generated by Django 3.0.3 on 2020-02-09 12:08

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        ('jeju2020', '0018_auto_20200206_0024'),
    ]

    operations = [
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
