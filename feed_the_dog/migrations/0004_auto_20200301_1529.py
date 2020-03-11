# Generated by Django 3.0 on 2020-03-01 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed_the_dog', '0003_dog_ownership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='who',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]