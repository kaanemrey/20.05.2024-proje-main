# Generated by Django 4.2.11 on 2024-06-14 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Base", "0003_rename_icerik_mesaj_içerik"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mesaj", old_name="içerik", new_name="icerik",
        ),
    ]
