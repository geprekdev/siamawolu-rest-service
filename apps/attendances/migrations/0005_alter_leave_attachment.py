# Generated by Django 3.2.13 on 2022-09-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0004_alter_leave_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='attachment',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]
