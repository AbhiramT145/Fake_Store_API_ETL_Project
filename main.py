from extract import extract_product, extract_users
from transform import transform_product, transform_users
from load import load_to_postgres

from logger import logger


def run_pipeline():
    """
    Run the complete ETL pipeline.
    """

    logger.info("=" * 50)
    logger.info("ETL Pipeline Started")
    logger.info("=" * 50)

    try:
        # Extract
        product_df = extract_product()
        user_df = extract_users()

        # Transform
        product_df = transform_product(product_df)
        user_df = transform_users(user_df)

        # Load
        load_to_postgres(product_df, "products")
        load_to_postgres(user_df, "users")

        logger.info("ETL Pipeline Completed Successfully.")

    except Exception:
        logger.exception("ETL Pipeline Failed.")
        raise


if __name__ == "__main__":
    run_pipeline()