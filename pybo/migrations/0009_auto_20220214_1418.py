# Generated by Django 3.1.3 on 2022-02-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_remove_mastery_user_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mastery_user',
            name='telephone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
