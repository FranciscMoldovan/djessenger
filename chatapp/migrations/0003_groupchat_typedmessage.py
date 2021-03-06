# Generated by Django 3.2.8 on 2021-10-18 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_chatuser_django_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypedMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mymessage', to='chatapp.chatuser')),
            ],
        ),
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='chatapp.typedmessage')),
            ],
        ),
    ]
