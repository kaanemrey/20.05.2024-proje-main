# Generated by Django 4.2.11 on 2024-06-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Base", "0012_alter_derstalepleri_ders_tipi_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="derstalepleri",
            name="ders_tipi",
            field=models.CharField(
                blank=True,
                choices=[("online", "Online"), ("yuz_yuze", "Yüz Yüze")],
                default=None,
                max_length=50,
            ),
        ),
    ]
