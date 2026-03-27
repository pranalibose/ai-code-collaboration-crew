import pandas as pd
from typing import Iterator, Dict
from pydantic import BaseModel
from logging import getLogger

logger = getLogger(__name__)

class CSVData(BaseModel):
    id: int
    value: float

def read_csv_file(filepath: str) -> Iterator[CSVData]:
    """
    Reads a csv file into a pandas DataFrame, handles missing data and detects outliers.
    
    Args:
        filepath (str): Path to the csv file
    
    Returns:
        Iterator[CSVData]: An iterator of CSVData objects
    """
    try:
        df = pd.read_csv(filepath)
        
        # Detect outliers
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[~((df >= (Q1 - 1.5 * IQR)) & (df <= (Q3 + 1.5 * IQR)))]
        
        if not outliers.empty:
            logger.warning(f"Detected {outliers.shape[0]} outliers in the csv file.")
        
        # Handle missing data
        df.dropna(inplace=True)
        
        return (
            CSVData(id=row.id, value=row.value)
            for index, row in df.iterrows()
        )
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
    except pd.errors.ParserError:
        logger.error(f"Error parsing file: {filepath}")
    except Exception as e:
        logger.error(f"Error reading csv file: {filepath} - {e}")
    return []

import os
import psycopg2
from typing import List
from pydantic import BaseModel
from logging import getLogger

logger = getLogger(__name__)

class DBConfig(BaseModel):
    host: str
    database: str
    user: str
    password: str

class CSVData(BaseModel):
    id: int
    value: float

def connect_to_postgres() -> psycopg2.extensions.connection:
    """
    Connects to the postgres database.
    
    Returns:
        psycopg2.extensions.connection: A connection object to the postgres database
    """
    db_config = DBConfig(**os.environ["DATABASE_URL"].split("="))
    connection = psycopg2.connect(
        host=db_config.host,
        database=db_config.database,
        user=db_config.user,
        password=db_config.password
    )
    return connection

def write_to_postgres(connection: psycopg2.extensions.connection, data: List[CSVData]) -> None:
    """
    Writes the data to the postgres database.
    
    Args:
        connection (psycopg2.extensions.connection): A connection object to the postgres database
        data (List[CSVData]): A list of CSVData objects
    """
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO csv_table (id, value)
            VALUES (%s, %s)
        """
        psycopg2.extras.execute_batch(cursor, query, [(row.id, row.value) for row in data])
        connection.commit()
        logger.info("Data written to the postgres database.")
    except psycopg2.Error as e:
        logger.error(f"Error writing to the postgres database - {e}")
        connection.rollback()

from .postgres_writer import connect_to_postgres, write_to_postgres
from typing import List
from pydantic import BaseModel
from csv_reader import read_csv_file

class CSVData(BaseModel):
    id: int
    value: float

def process_csv_file(filepath: str) -> None:
    """
    Reads a csv file, handles missing data and outliers, and writes the data to the postgres database.
    
    Args:
        filepath (str): Path to the csv file
    """
    data = list(read_csv_file(filepath))
    connection = connect_to_postgres()
    write_to_postgres(connection, data)
    connection.close()

import os

class Config:
    CSV_FILEPATH = "/path/to/your/csv/file.csv"
    DATABASE_URL = os.environ["DATABASE_URL"]