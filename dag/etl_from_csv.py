import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator


default_args= {
    'owner': 'Abe',
    'start_date': datetime(2024, 8, 12) - timedelta(hours=7)
}

with DAG(
    'etl_csv_files',
    description='from gdrive to postgres',
    schedule_interval='@hourly',
    default_args=default_args, 
    catchup=False) as dag:
    files = {
        'stock' : 'https://drive.google.com/file/d/1oekl42aBVub7We2B6MJdijFYy64ftYAv/view?usp=sharing',
        'securities' : 'https://drive.google.com/file/d/1DmXCi5uVUZvx627wYZIiFuookqX9orQg/view?usp=sharing'
    }

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    def read_from_gdrive(url,file_name):
        url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
        df = pd.read_csv(url)
        print("Sample data :")
        print(df.head())
        df.to_csv(f'/opt/airflow/data/{file_name}.csv',index=False)

    @task()
    def get_files_stock():
        file_name = list(files.keys())[0]
        url = files['stock']
        df = read_from_gdrive(url,file_name)
        return df 

    @task()
    def get_files_security():
        file_name = list(files.keys())[1]
        url = files['securities']
        df = read_from_gdrive(url,file_name)
        return df
    
    @task()
    def combine_files():
        # Read the dataframes
        df_stock = pd.read_csv(f'/opt/airflow/data/{list(files.keys())[0]}.csv')
        df_securities = pd.read_csv(f'/opt/airflow/data/{list(files.keys())[1]}.csv')

        # Join df_customer and df_purchase on 'customer_id'
        df = pd.merge(df_stock, df_securities, left_on='symbol', right_on='Ticker symbol')

        print(df.head())
        df.to_csv(f'/opt/airflow/data/data_combine.csv', index=False)
    

    @task()
    def preprocess_data():
        df = pd.read_csv('/opt/airflow/data/data_combine.csv')
        df =  df[['date','symbol', 'Security', 'GICS Sector', 'GICS Sub Industry','open','close','low', 'high', 'volume']]
        df.columns = df.columns.str.strip()  # Hapus spasi/tab di awal/akhir
        df.columns = df.columns.str.lower()  # Ubah menjadi lowercase
        df.columns = df.columns.str.replace(' ', '_')  # Ganti spasi dengan underscore
        df.to_csv(f'/opt/airflow/data/stock_clean.csv', index=False)
    start >> [get_files_stock(), get_files_security()] >> combine_files() >> preprocess_data() >> end