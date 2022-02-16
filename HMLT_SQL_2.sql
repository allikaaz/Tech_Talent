create database customers;
create table customers(
customerID int not null,
first_name varchar(100) not null,
surname varchar(100) not null,
house_number int not null,
Address varchar (100) not null,
postcode char (80) not null,
primary key(customerID));

-- creating ordering table

CREATE TABLE orders(
OrderID INT NOT NULL PRIMARY KEY,
CustomerID INT, 
Order_Date varchar(100),
Dispatch_Date varchar(100),
Due_Date varchar(80)
);

explain customers;

explain orders;

-- adding values into the customers tables

INSERT INTO customers (Customer_id, first_name, surname, house_number, Address, Postcode)
VALUES
(1, "Suzannah", "Downie", "1", "Database road", "FP12 1DE"),
(2, "Georgina", "Stanley", "65", "String Lane", "LA76 8ZS"),
(3, "Andy", "Gray", "42", "Data Street", "SQ57 4TP"),
(4, "Satinder", "Sohal", "34", "Boolen Way", "TP67 9QO"),
(5, "Joe", "Bloggs", "119", "Integer Avenue", "AC12 FPU"),
(6, "Kazeem", "Alli", "121", "Beaconsfield Street", "NE48 5JQ")
;
select * from customers;
-- customers table having 10 records

INSERT INTO customers (Customer_id, first_name, surname, house_number, Address, Postcode)
VALUES
(7, "Saidat", "Rabiu", "187", "Wingrove road", "FP13 2SE"),
(8, "Usman", "Dahiru", "129", "crystal palace", "PA76 8ZF"),
(9, "Andy", "Carol", "22", "Data Road", "SQ87 5JP"),
(10, "Adam", "Harvey", "134", "Boolen Street", "GP67 9QY")
;
select * from customers;

-- adding values into orders table

INSERT INTO orders (OrderID, CustomerID, Order_Date, Dispatch_Data, Due_Date)
VALUES
(1, "5", "11/04/2021", "13/05/2021", "14/05/2021"),
(2, "43", "15/04/2021", "13/05/2021", "14/05/2021"),
(3, "12", "20/04/2021", "13/05/2021", "14/05/2021"),
(4, "5", "20/04/2021", "13/05/2021", "14/05/2021")
;

explain orders;
select * from orders;

-- updating the customers record
UPDATE customers
SET surname = 'AlliK'
WHERE customer_id = 7;

SELECT * FROM customers;

-- deleting from the customers record
DELETE FROM customers 
WHERE customer_id ='2';

SELECT * FROM customers;

-- joining tables

SELECT customers.Customer_id , orders.CustomerID
FROM customers
INNER JOIN orders
ON customers.Customer_id = orders.CustomerID;

-- running simple query 
SELECT * FROM customers
WHERE customers.Customer_id = "7";

-- running complex query 
SELECT * FROM customers, orders
WHERE customers.Customer_id = orders.CustomerID AND customers.Address= "Integer Avenue";

-- sorting order by surname
SELECT * FROM customers ORDER BY surname;

-- sorting order by house number
SELECT * FROM customers ORDER BY house_number;

-- select using comparison operators
SELECT * FROM customers
WHERE house_number between 30 and 130;
