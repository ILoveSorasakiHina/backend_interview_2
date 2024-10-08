# Generated by Django 5.1.1 on 2024-09-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("DataGovCRUD", "0005_alter_event_uid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="hit_rate",
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name="event",
            name="uid",
            field=models.CharField(
                db_index=True,
                max_length=50,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
