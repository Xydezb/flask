# Generated by Django 2.0.7 on 2019-05-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20190527_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('TRADE_CLOSE', '交易关闭'), ('TRADE_SUCCESS', '成功'), ('TRADE_FINISHED', '交易结束'), ('WAIT_BUYER_PAY', '交易创建'), ('paying', '待支付')], default='paying', max_length=20, verbose_name='交易状态'),
        ),
    ]