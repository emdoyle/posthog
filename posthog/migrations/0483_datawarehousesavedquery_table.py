# Generated by Django 4.2.15 on 2024-10-01 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("posthog", "0482_alertconfiguration_calculation_interval_and_more"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AddField(
                    model_name="datawarehousesavedquery",
                    name="table",
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="posthog.datawarehousetable",
                    ),
                ),
            ],
            database_operations=[
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_datawarehousesavedquery" ADD COLUMN "table_id" uuid NULL CONSTRAINT "posthog_datawarehous_table_id_96fdb4f5_fk_posthog_d" REFERENCES "posthog_datawarehousetable"("id") DEFERRABLE INITIALLY DEFERRED; -- existing-table-constraint-ignore
                    SET CONSTRAINTS "posthog_datawarehous_table_id_96fdb4f5_fk_posthog_d" IMMEDIATE; -- existing-table-constraint-ignore
                    """,
                    reverse_sql="""
                    ALTER TABLE "posthog_datawarehousesavedquery" DROP COLUMN IF EXISTS "table_id";
                    """,
                ),
                migrations.RunSQL(
                    """
                    CREATE INDEX CONCURRENTLY "posthog_datawarehousesavedquery_table_id_96fdb4f5" ON "posthog_datawarehousesavedquery" ("table_id");
                    """,
                    reverse_sql="""
                    DROP INDEX IF EXISTS "posthog_datawarehousesavedquery_table_id_96fdb4f5";
                    """,
                ),
            ],
        ),
    ]