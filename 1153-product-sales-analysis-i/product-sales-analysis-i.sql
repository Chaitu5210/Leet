# Write your MySQL query statement below
select product_name, year, price
from Product
join Sales
ON Product.product_id = Sales.product_id