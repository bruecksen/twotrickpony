# Generated by Django 4.0.8 on 2023-02-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_homepage_thank_you_email_text_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='thank_you_email_text',
            field=models.TextField(blank=True),
        ),
    ]
