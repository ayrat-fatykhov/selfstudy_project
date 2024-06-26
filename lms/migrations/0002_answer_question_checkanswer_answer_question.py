# Generated by Django 4.2.13 on 2024-06-25 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=255, verbose_name='ответ пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='вопрос')),
                ('right_answer', models.CharField(max_length=255, verbose_name='правильный ответ')),
            ],
        ),
        migrations.CreateModel(
            name='CheckAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_right', models.BooleanField(default=False, verbose_name='ответ верный')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.answer', verbose_name='ответ пользователя')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.question', verbose_name='вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.question', verbose_name='вопрос'),
        ),
    ]
