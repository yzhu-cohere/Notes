%%configure -f
{ "conf": {
    "spark.pyspark.python": "python3",
    "spark.pyspark.virtualenv.enabled": "true",
    "spark.sql.parquet.writeLegacyFormat": "true",
    "spark.sql.parquet.enableVectorizedReader":"false",
    "spark.pyspark.virtualenv.type":"native",
    "spark.pyspark.virtualenv.bin.path":"/usr/bin/virtualenv",
    "spark.jars":"s3://aws-glue-assets-137931813934-us-east-2/extraJars/hudi-spark3-bundle_2.12-0.11.1.jar",
    "spark.serializer":"org.apache.spark.serializer.KryoSerializer",
    "spark.sql.hive.convertMetastoreParquet":"false",
    "spark.sql.extensions": "org.apache.spark.sql.hudi.HoodieSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
    "hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory",
    "spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive":"true"
    }
}