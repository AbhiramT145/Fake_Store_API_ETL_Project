-- =====================================================
-- Fake Store API ETL Project
-- SQL Analysis
-- Database: PostgreSQL
-- =====================================================


-- =====================================================
-- 1. PRODUCT ANALYSIS
-- =====================================================

-- 1.1 Total Number of Products

SELECT COUNT(*) AS total_products
FROM products;


-- -----------------------------------------------------

-- 1.2 Number of Products by Category

SELECT
    product_category,
    COUNT(*) AS total_products
FROM products
GROUP BY product_category
ORDER BY total_products DESC;


-- -----------------------------------------------------

-- 1.3 Average Product Price by Category

SELECT
    product_category,
    ROUND(AVG(product_price)::numeric, 2) AS average_price
FROM products
GROUP BY product_category
ORDER BY average_price DESC;


-- -----------------------------------------------------

-- 1.4 Top 5 Most Expensive Products

SELECT
    product_name,
    product_category,
    product_price
FROM products
ORDER BY product_price DESC
LIMIT 5;


-- -----------------------------------------------------

-- 1.5 Cheapest Product

SELECT
    product_name,
    product_category,
    product_price
FROM products
ORDER BY product_price ASC
LIMIT 1;


-- -----------------------------------------------------

-- 1.6 Products Priced Above the Overall Average

SELECT
    product_name,
    product_category,
    product_price
FROM products
WHERE product_price >
(
    SELECT AVG(product_price)
    FROM products
)
ORDER BY product_price DESC;


-- =====================================================
-- 2. USER ANALYSIS
-- =====================================================

-- 2.1 Total Number of Users

SELECT COUNT(*) AS total_users
FROM users;


-- -----------------------------------------------------

-- 2.2 Number of Users by City

SELECT
    city,
    COUNT(*) AS total_users
FROM users
GROUP BY city
ORDER BY total_users DESC;


-- -----------------------------------------------------

-- 2.3 Number of Users by Zipcode

SELECT
    zipcode,
    COUNT(*) AS total_users
FROM users
GROUP BY zipcode
ORDER BY total_users DESC;


-- -----------------------------------------------------

-- 2.4 User Directory

SELECT
    first_name,
    last_name,
    username,
    user_email,
    city
FROM users
ORDER BY last_name, first_name;