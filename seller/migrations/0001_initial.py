# Generated by Django 4.2.1 on 2023-08-07 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "item_name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "main_genre_name",
                    models.CharField(
                        choices=[
                            ("Grains", "穀物類"),
                            ("Vegetables", "野菜類"),
                            ("Fruits", "果物類"),
                            ("Others", "その他"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "sub_genre_name",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("---", "---"),
                            ("LeafStem", "葉茎菜類"),
                            ("Root", "根菜類"),
                            ("Fruit", "果菜類"),
                            ("Others", "その他"),
                        ],
                        default="---",
                        max_length=100,
                    ),
                ),
            ],
            options={"permissions": [("can_edit_product", "Can edit product")],},
        ),
        migrations.CreateModel(
            name="Seller",
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
                ("address", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vegetable",
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
                ("item_type", models.CharField(default="---", max_length=100)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=100),
                ),
                ("content_quantity", models.PositiveIntegerField(default=1)),
                (
                    "content_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=100),
                ),
                ("total_quantity", models.PositiveIntegerField(default=0)),
                (
                    "item_name",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="seller.product",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vegetable",
                        to="seller.seller",
                    ),
                ),
            ],
        ),
    ]
