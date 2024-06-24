from setuptools import find_packages, setup

setup(
    name="dagster_airbyte_dbt",
    packages=find_packages(exclude=["dagster_airbyte_dbt_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-airbyte",
        "dagster-dbt",
        "dagster-duckdb",
        "dbt-core",
        "dbt-duckdb",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
