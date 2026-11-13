# SQL Analysis Report

## Overview

This report presents the results of SQL queries executed on the PostgreSQL database after loading data from the Fake Store API using the ETL pipeline. The analysis focuses on product information and user demographics to validate the loaded data and demonstrate SQL querying skills.

---

# Product Analysis

## Total Products

| Metric | Value |
|--------|------:|
| Total Products | 20 |

### Insight

The **products** table contains **20 products**, confirming that all product records were successfully loaded into the PostgreSQL database during the ETL process.

---

## Products by Category

| Category | Number of Products |
|----------|-------------------:|
| Women's Clothing | 6 |
| Electronics | 6 |
| Men's Clothing | 4 |
| Jewelery | 4 |

### Insight

The product catalog is distributed across **four categories**. **Women's Clothing** and **Electronics** each contain **6 products**, making them the largest categories in the dataset, while **Men's Clothing** and **Jewelery** each contain **4 products**.

This distribution indicates a relatively balanced dataset with no single category overwhelmingly dominating the catalog.

---

## Average Product Price by Category

| Category | Average Price (USD) |
|----------|--------------------:|
| Electronics | $332.50 |
| Jewelery | $221.00 |
| Men's Clothing | $51.06 |
| Women's Clothing | $26.29 |

### Insight

The **Electronics** category has the highest average product price at **$332.50**, followed by **Jewelery** at **$221.00**. In contrast, **Men's Clothing** and **Women's Clothing** have significantly lower average prices, averaging **$51.06** and **$26.29**, respectively.

This indicates that electronic products are considerably more expensive than products in the clothing categories, resulting in a wide price variation across the product catalog.

---

## Highest-Priced Products

| Rank | Product | Category | Price (USD) |
|-----:|---------|----------|------------:|
| 1 | Samsung 49-Inch CHG90 Curved Gaming Monitor | Electronics | $999.99 |
| 2 | John Hardy Women's Legends Naga Bracelet | Jewelery | $695.00 |
| 3 | Acer SB220Q 21.5" Full HD IPS Monitor | Electronics | $599.00 |
| 4 | Solid Gold Petite Micropave | Jewelery | $168.00 |

### Insight

The highest-priced products are concentrated in the **Electronics** and **Jewelery** categories. Electronics account for **two** of the four highest-priced products, including the most expensive item in the dataset, while Jewelery contributes the remaining two. This aligns with the earlier finding that these categories have substantially higher average prices than the clothing categories.

---

## Cheapest Product

| Product | Category | Price (USD) |
|---------|----------|------------:|
| Opna Women's Short Sleeve Moisture | Women's Clothing | $7.95 |

### Insight

The least expensive product in the dataset is **Opna Women's Short Sleeve Moisture**, priced at **$7.95**. This product belongs to the **Women's Clothing** category, reinforcing the earlier observation that clothing items are generally the most affordable products in the catalog.

---

# User Analysis

## Total Users

| Metric | Value |
|--------|------:|
| Total Users | 10 |

### Insight

The **users** table contains **10 user records**, confirming that all user data was successfully loaded into the PostgreSQL database during the ETL process.

---

## User Distribution by City

| City | Number of Users |
|------|----------------:|
| Kilcoole | 2 |
| Fort Wayne | 1 |
| San Antonio | 1 |
| Miami | 1 |
| Fresno | 1 |
| El Paso | 1 |
| san Antonio | 1 |
| Cullman | 1 |
| Mesa | 1 |

### Insight

The user dataset contains records from **9 cities**, with **Kilcoole** having the highest number of users (**2**). All other cities contain a single user, indicating that the dataset is geographically distributed rather than concentrated in one location.

The analysis also reveals a **data quality issue**: both **"San Antonio"** and **"san Antonio"** appear as separate values due to inconsistent capitalization. In a production ETL pipeline, this inconsistency should be resolved during the transformation stage by standardizing text fields before loading the data into the database.

---

## User Distribution by Zipcode

| Zipcode | Number of Users |
|---------|----------------:|
| 96378-0245 | 3 |
| 12926-3874 | 2 |
| 12346-0456 | 1 |
| 29567-1452 | 1 |
| 98234-1734 | 1 |
| 10256-4532 | 1 |
| 80796-1234 | 1 |

### Insight

The users in the dataset are distributed across **7 unique zipcodes**. The zipcode **96378-0245** contains the highest number of users (**3**), followed by **12926-3874** with **2** users. The remaining zipcodes each contain a single user, indicating that the dataset represents users from multiple geographic regions.

---

# SQL Concepts Demonstrated

The SQL analysis demonstrates the use of the following PostgreSQL concepts:

- SELECT
- COUNT()
- AVG()
- GROUP BY
- ORDER BY
- LIMIT
- Aggregate Functions
- ROUND()
- Subqueries

---

# Conclusion

The SQL analysis validates that the ETL pipeline successfully extracted data from the Fake Store API, transformed it using Pandas, and loaded it into PostgreSQL. The analysis provided insights into product distribution, pricing trends, and user demographics while demonstrating the use of core SQL concepts such as aggregation, grouping, sorting, limiting, and subqueries.

Additionally, the analysis identified a data quality issue involving inconsistent capitalization of city names (e.g., **"San Antonio"** and **"san Antonio"**). This highlights the importance of performing data cleaning and standardization during the transformation stage of an ETL pipeline.

Overall, this project demonstrates an end-to-end ETL workflow using Python, Pandas, PostgreSQL, and SQL for data extraction, transformation, loading, and analytical reporting.