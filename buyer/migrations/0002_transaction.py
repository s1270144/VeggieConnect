# Generated by Django 4.2.1 on 2023-08-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("buyer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("purchase_id", models.CharField(max_length=100, unique=True)),
                ("purchase_status", models.CharField(max_length=50)),
                ("payment_method", models.CharField(max_length=50)),
                ("shipping_info", models.TextField()),
                ("billing_info", models.TextField()),
                ("additional_info", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
