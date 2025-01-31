# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

DA = DBAcademyHelper(**helper_arguments)

DA.validate_datasets(fail_fast=True, repairing_dataset=False)

DA.publisher = Publisher()

DA.conclude_setup()

