import pandas as pd

from logger import logger


def transform_product(product_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform product data.
    """

    logger.info("Starting product transformation.")

    try:
        df = product_df.copy()

        logger.info("Renaming product columns.")

        df = df.rename(columns={
            "id": "product_id",
            "title": "product_name",
            "price": "product_price",
            "category": "product_category",
            "description": "description"
        })

        logger.info("Selecting required product columns.")

        df = df[
            [
                "product_id",
                "product_name",
                "product_price",
                "product_category",
                "description"
            ]
        ]

        logger.info("Converting product_price to float.")

        df["product_price"] = df["product_price"].astype(float)

        logger.info(f"Product transformation completed successfully. Total rows: {len(df)}")

        return df

    except Exception:
        logger.exception("Product transformation failed.")
        raise


def transform_users(user_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform user data.
    """

    logger.info("Starting user transformation.")

    try:
        df = user_df.copy()

        logger.info("Extracting nested name fields.")

        df["first_name"] = df["name"].apply(lambda x: x["firstname"])
        df["last_name"] = df["name"].apply(lambda x: x["lastname"])

        logger.info("Extracting nested address fields.")

        df["street"] = df["address"].apply(lambda x: x["street"])
        df["city"] = df["address"].apply(lambda x: x["city"])
        df["zipcode"] = df["address"].apply(lambda x: x["zipcode"])

        logger.info("Renaming user columns.")

        df = df.rename(columns={
            "id": "user_id",
            "email": "user_email",
            "username": "username"
        })

        logger.info("Selecting required user columns.")

        df = df[
            [
                "user_id",
                "user_email",
                "username",
                "first_name",
                "last_name",
                "street",
                "city",
                "zipcode"
            ]
        ]

        logger.info(f"User transformation completed successfully. Total rows: {len(df)}")

        return df

    except Exception:
        logger.exception("User transformation failed.")
        raise