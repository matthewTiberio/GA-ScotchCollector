# Generated by Django 4.1.3 on 2022-11-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scotch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('HL', 'Highland'), ('IS', 'Islay'), ('LL', 'Lowland'), ('SS', 'Speyside')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volume', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]