
from dagster import AssetExecutionContext
from dagster_dbt.asset_decorator import dbt_assets
import os
from dagster_dbt import DbtProject, DbtCliResource, DagsterDbtTranslatorSettings
from pathlib import Path



dbt_project_path = Path(__file__).parent.joinpath("analytics")
DBT_PROJECT_DIR = os.fspath(dbt_project_path)

dbt_project = DbtProject(
    project_dir=dbt_project_path,
    state_path="target/slim_ci",
    target="dev",
)

DBT_MANIFEST = dbt_project.manifest_path

@dbt_assets(
    manifest=DBT_MANIFEST,
)
def all_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    dbt_cli_task = dbt.cli(["build"], context=context)
    yield from dbt_cli_task.stream()#.fetch_row_counts()
    #.fetch_row_counts()
       
