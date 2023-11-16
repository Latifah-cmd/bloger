# Generated by Django 3.2.20 on 2023-11-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Author Name')),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=300)),
                ('address', models.CharField(blank=True, default='N/A', max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'female')], max_length=2)),
            ],
        ),
    ]