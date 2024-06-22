# Generated by Django 4.2.11 on 2024-06-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Base", "0004_rename_içerik_mesaj_icerik"),
    ]

    operations = [
        migrations.AddField(
            model_name="derstalepleri",
            name="ders_tipi",
            field=models.CharField(
                choices=[("online", "Online"), ("yuz_yuze", "Yüz Yüze")],
                default="online",
                max_length=50,
            ),
        ),
    ]
