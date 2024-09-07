# Generated by Django 5.1 on 2024-09-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_portfolio_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_document',
            field=models.FileField(blank=True, null=True, upload_to='kyc_documents/'),
        ),
        migrations.AddField(
            model_name='user',
            name='kyc_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='portfolio_balance',
            field=models.DecimalField(decimal_places=2, default=100000.0, max_digits=15),
        ),
    ]
