spark.sql("REFRESH TABLE analytics_dw_dev.hudi_raw_servicerequest")
spark.sql("REFRESH TABLE analytics_dw_dev.hudi_raw_authorization")
spark.sql("REFRESH TABLE analytics_dw_dev.ghp_auth_file_integration_qc")