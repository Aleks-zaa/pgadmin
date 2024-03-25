-- SQL-команды для создания таблиц
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(250),
    last_name VARCHAR(250),
    title VARCHAR(250),
    birth_date date,
    notes TEXT
);

SELECT * FROM employees

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(250),
    contact_name VARCHAR(250)
);

SELECT * FROM customers

CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10) REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(25)
);