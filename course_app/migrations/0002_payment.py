# Generated by Django 4.2.5 on 2023-09-27 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('наличные', 'наличные'), ('перевод на счет', 'перевод на счет')], max_length=50, verbose_name='способ оплаты')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('amount', models.FloatField(verbose_name='сумма оплаты')),
                ('course', models.ForeignKey(blank=True, db_column='course', null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.course', to_field='title', verbose_name='оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, db_column='lesson', null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email', verbose_name='пользователь')),
            ],
        ),
    ]
