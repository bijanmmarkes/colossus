# Generated by Django 2.0.6 on 2018-06-05 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_campaign_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='mailing_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='lists.MailingList', verbose_name='mailing list'),
        ),
    ]
