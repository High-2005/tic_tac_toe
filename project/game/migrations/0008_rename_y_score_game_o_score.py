# Generated by Django 4.2.4 on 2023-08-30 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_game_x_score_alter_game_y_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='y_score',
            new_name='o_score',
        ),
    ]
