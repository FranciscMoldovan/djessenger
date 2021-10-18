# Generated by Django 3.2.8 on 2021-10-18 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_groupchat_typedmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupchat',
            name='posts',
        ),
        migrations.AddField(
            model_name='typedmessage',
            name='chat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chat_from', to='chatapp.groupchat'),
            preserve_default=False,
        ),
    ]