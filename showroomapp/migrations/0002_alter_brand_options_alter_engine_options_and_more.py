# Generated by Django 4.2.3 on 2023-07-26 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("showroomapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brand",
            options={"verbose_name_plural": "Brand"},
        ),
        migrations.AlterModelOptions(
            name="engine",
            options={"verbose_name_plural": "Engine"},
        ),
        migrations.AlterModelOptions(
            name="feature",
            options={"verbose_name_plural": "Feature"},
        ),
        migrations.AlterModelOptions(
            name="model",
            options={"verbose_name_plural": "Model"},
        ),
        migrations.AlterModelOptions(
            name="showroom",
            options={"verbose_name_plural": "showroom"},
        ),
        migrations.AlterModelOptions(
            name="staff",
            options={"verbose_name_plural": "Staff"},
        ),
        migrations.RenameField(
            model_name="showroom",
            old_name="location",
            new_name="address",
        ),
    ]
