import os
import findspark
from spark_builder import SparkBuilder
from data_processing import DataProcessing
from pyspark.sql.functions import explode, split, col
import yaml
import sys
from logger import Logger

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

cfg = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)
logger = Logger(show=True)
log = logger.get_logger(__name__)

if __name__ == '__main__':
    spark = SparkBuilder({'spark.app.name': 'Clustering'}).getSession()

    cfg = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)

    processing = DataProcessing(spark)

    dataset = processing.load()

    table_struct = ', '.join([f'`{col}` FLOAT'for col in dataset.columns])
    url = f"jdbc:oracle:thin:@{cfg['db_connection']['host']}:1521/FREE"
    properties = {
        "user": "system",
        "password": str(cfg['db_connection']['pass']),
        "driver": "oracle.jdbc.driver.OracleDriver"
    }

    dataset.write.option("createTableColumnTypes", table_struct).jdbc(
        url=url, table=cfg['db']['data_table'], mode="overwrite", properties=properties)
    log.info(f'Dataset uploaded to db: {table_struct}')
    del(dataset)

    dataset = spark.read.jdbc(url=url, table=cfg['db']['data_table'], properties=properties)
    vec_dataset = processing.vectorize(dataset)
    scaled_dataset = processing.scale(vec_dataset)
    predictions, score = processing.cluster(scaled_dataset)


    predictions.select(['prediction']).write.jdbc(
        url=url, table=cfg['db']['pred_table'], mode='append', properties=properties)
    log.info(f'Predictions saved')
    
    spark.stop()