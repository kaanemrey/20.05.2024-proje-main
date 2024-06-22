# Generated by Django 4.2.11 on 2024-06-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Base", "0016_alter_verilendersler_ders_tipi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verilendersler",
            name="ders_tipi",
            field=models.CharField(
                choices=[("online", "Online"), ("yuz_yuze", "Yüz Yüze")],
                default="",
                max_length=50,
            ),
        ),
    ]
