# Generated by Django 4.0.4 on 2022-05-02 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_favs_user_fav'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fav',
            new_name='favs',
        ),
    ]
