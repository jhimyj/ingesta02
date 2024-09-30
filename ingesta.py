import pandas as pd
import boto3
from sqlalchemy import create_engine

def export_mysql_to_s3(host, port, user, password, database, table, output_file, bucket_name):
    try:
        connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)
        df = pd.read_sql(f"SELECT * FROM {table}", engine)
        df.to_csv(output_file, index=False)
        s3_client = boto3.client('s3')
        s3_client.upload_file(output_file, bucket_name, output_file)

        print("Ingesta completada")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
export_mysql_to_s3('34.201.237.57', 8005, 'root', 'utec', 'tienda', 'fabricantes', 'data.csv', 'ingestajhimy')
