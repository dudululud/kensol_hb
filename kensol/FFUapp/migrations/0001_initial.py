# Generated by Django 4.2.4 on 2023-08-14 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Estimate",
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
                ("size", models.CharField(max_length=50)),
                ("motorType", models.CharField(max_length=50)),
                ("spec", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="MaterialCost",
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
                ("won_per_kg", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="MaterialSize",
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
                ("width", models.FloatField()),
                ("length", models.FloatField()),
                ("manufacture_quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PaintCost",
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
                ("won_per_square_meter", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="PlanarFigureSize",
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
                ("width", models.FloatField()),
                ("length", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="RawMaterial",
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
                ("quality", models.CharField(max_length=50)),
                ("weight", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="RawMaterialThickness",
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
                ("thickness", models.FloatField()),
                (
                    "raw_material",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="FFUapp.rawmaterial",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Option",
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
                ("item", models.CharField(max_length=50)),
                ("necessary_quantity", models.IntegerField()),
                (
                    "estimate",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="option",
                        to="FFUapp.estimate",
                    ),
                ),
                (
                    "material_cost",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="option",
                        to="FFUapp.materialcost",
                    ),
                ),
                (
                    "material_size",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="option",
                        to="FFUapp.materialsize",
                    ),
                ),
                (
                    "paint_cost",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="option",
                        to="FFUapp.paintcost",
                    ),
                ),
                (
                    "planar_figure_size",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="option",
                        to="FFUapp.planarfiguresize",
                    ),
                ),
                (
                    "raw_material_thickness",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="FFUapp.rawmaterialthickness",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Casing",
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
                ("item", models.CharField(max_length=50)),
                ("necessary_quantity", models.IntegerField()),
                (
                    "estimate",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="casings",
                        to="FFUapp.estimate",
                    ),
                ),
                (
                    "material_cost",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="casing",
                        to="FFUapp.materialcost",
                    ),
                ),
                (
                    "material_size",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="casing",
                        to="FFUapp.materialsize",
                    ),
                ),
                (
                    "paint_cost",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="casing",
                        to="FFUapp.paintcost",
                    ),
                ),
                (
                    "planar_figure_size",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="casing",
                        to="FFUapp.planarfiguresize",
                    ),
                ),
                (
                    "raw_material_thickness",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="FFUapp.rawmaterialthickness",
                    ),
                ),
            ],
        ),
    ]
