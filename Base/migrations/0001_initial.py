# Generated by Django 4.2.11 on 2024-06-13 11:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ders", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Dil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dil", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Sehir",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sehir", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="VerilenDersler",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "saatlik_ucret",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "ders_seviyesi",
                    models.CharField(
                        choices=[
                            ("İlkokul", "İlkokul"),
                            ("Ortaokul", "Ortaokul"),
                            ("Lise", "Lise"),
                            ("Universite", "Üniversite"),
                            ("Yukseklisans", "Yüksek Lisans"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "ders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Base.ders"
                    ),
                ),
                (
                    "ders_dili",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Base.dil"
                    ),
                ),
                (
                    "egitmen",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sehir",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Base.sehir"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sohbet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user1_sohbet",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user2_sohbet",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "kullanici_tipi",
                    models.CharField(
                        choices=[("egitmen", "Eğitmen"), ("ogrenci", "Öğrenci")],
                        max_length=50,
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, default=None, max_length=200, null=True
                    ),
                ),
                (
                    "profil_foto",
                    models.ImageField(blank=True, null=True, upload_to="avatarlar"),
                ),
                (
                    "cinsiyet",
                    models.CharField(
                        choices=[("erkek", "Erkek"), ("kadin", "Kadın")], max_length=50
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OgrenciProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "seviye",
                    models.CharField(
                        choices=[
                            ("ilkokul", "İlkokul"),
                            ("ortaokul", "Ortaokul"),
                            ("lise", "Lise"),
                            ("universite", "Üniversite"),
                            ("yukseklisans", "Yüksek Lisans"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Base.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mesaj",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tarih", models.DateTimeField(auto_now_add=True)),
                ("içerik", models.CharField(max_length=200)),
                (
                    "alici",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alınan_mesajlar",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "gönderen",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gönderilen_mesajlar",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sohbet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="Base.sohbet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EgitmenProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="Base.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DersTalepleri",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("baslik", models.CharField(max_length=50)),
                ("talep_notu", models.TextField(blank=True, max_length=200, null=True)),
                ("talep_durumu", models.BooleanField(default=False)),
                (
                    "min_butce",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "max_butce",
                    models.IntegerField(
                        validators=[django.core.validators.MaxValueValidator(10000)]
                    ),
                ),
                (
                    "ogrenci_seviyesi",
                    models.CharField(
                        choices=[
                            ("İlkokul", "İlkokul"),
                            ("Ortaokul", "Ortaokul"),
                            ("Lise", "Lise"),
                            ("Üniversite", "Üniversite"),
                            ("Yüksek Lisans", "Yüksek Lisans"),
                        ],
                        max_length=50,
                    ),
                ),
                ("olusturulma_tarihi", models.DateTimeField(auto_now_add=True)),
                ("gunceleme", models.DateTimeField(auto_now=True)),
                (
                    "ders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Base.ders"
                    ),
                ),
                (
                    "dil",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Base.dil",
                    ),
                ),
                (
                    "konum",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Base.sehir",
                    ),
                ),
                (
                    "kullanici",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
