from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

from logger import logger

from config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)


def load_to_postgres(df: pd.DataFrame, table_name: str) -> None:
    """
    Load a DataFrame into a PostgreSQL table.
    """

    logger.info(f"Starting data load into '{table_name}' table.")

    engine = None

    try:
        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            )

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        logger.info(
            f"Successfully loaded {len(df)} records into '{table_name}'."
        )

    except SQLAlchemyError:
        logger.exception(
            f"Failed to load data into '{table_name}'."
        )
        raise

    finally:
        if engine is not None:
            engine.dispose()
            logger.info("Database connection closed.")