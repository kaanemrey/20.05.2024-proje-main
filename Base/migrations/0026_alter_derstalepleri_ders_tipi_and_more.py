# Generated by Django 4.2.11 on 2024-06-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Base", "0025_alter_derstalepleri_ders_tipi"),
    ]

    operations = [
        migrations.AlterField(
            model_name="derstalepleri",
            name="ders_tipi",
            field=models.CharField(
                blank=True,
                choices=[
                    ("online", "Online"),
                    ("yuz_yuze", "Yüz Yüze"),
                    (None, "Online ve Yüz Yüze"),
                ],
                default=None,
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="verilendersler",
            name="ders_tipi",
            field=models.CharField(
                blank=True,
                choices=[
                    ("online", "Online"),
                    ("yuz_yuze", "Yüz Yüze"),
                    (None, "Online ve Yüz Yüze"),
                ],
                default=None,
                max_length=50,
                null=True,
            ),
        ),
    ]
