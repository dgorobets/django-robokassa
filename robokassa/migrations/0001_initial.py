# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('InvId', models.IntegerField(verbose_name='Номер заказа', db_index=True)),
                ('OutSum', models.CharField(verbose_name='Сумма', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время получения уведомления')),
            ],
            options={
                'verbose_name': 'Уведомление об успешном платеже',
                'verbose_name_plural': 'Уведомления об успешных платежах (ROBOKASSA)',
            },
        ),
    ]
