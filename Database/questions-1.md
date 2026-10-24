# SQL Practice — Online Store Database

## Database
Tables:
- customers(customer_id, first_name, last_name, email, city)
- products(product_id, product_name, category, price, stock)
- orders(order_id, customer_id, order_date, status)
- order_items(order_item_id, order_id, product_id, quantity)
- addresses(address_id, customer_id, city, country)

Relationship:
customers -> orders -> order_items -> products
customers -> addresses

---

# Level 1 — SELECT / WHERE

1. Display all customers.
2. Display only first_name and last_name from customers.
3. Display all products.
4. Find products with price greater than 5000.
5. Find customers who live in Dhaka.
6. Find products whose stock is less than 20.
7. Find all orders with status = 'Delivered'.
8. Find products in the 'Electronics' category.
9. Find customers whose first_name starts with 'A'.
10. Find products with price between 2000 and 10000.

# Level 2 — ORDER BY / LIMIT / DISTINCT

11. Display products from most expensive to cheapest.
12. Display the 5 cheapest products.
13. Display the 3 products with the highest stock.
14. Show all different customer cities.
15. Show all different product categories.
16. Find the most expensive product.
17. Find the cheapest product.
18. Find the 5 most recent orders.
19. Sort customers alphabetically by last_name.
20. Display products alphabetically by product_name.

# Level 3 — Aggregate Functions / GROUP BY

21. Count the total number of customers.
22. Count the total number of products.
23. Find the average product price.
24. Find the maximum product price.
25. Find the minimum product price.
26. Find the total number of orders.
27. Count how many orders have each status.
28. Count how many customers are in each city.
29. Find the average price for each product category.
30. Find the total stock available for each category.
31. Find categories containing more than 2 products.
32. Find cities having more than 2 customers.

# Level 4 — JOIN

33. Display each order_id together with the customer's first and last name.
34. Display customer name and order date.
35. Display order_id, product_name and quantity.
36. Display customer name, product name and quantity.
37. Display customer name, product name, quantity and product price.
38. Find all orders made by customers from Dhaka.
39. Find all products ordered by Sohel.
40. Show every customer and their orders, including customers who have never placed an order.
41. Show every product and the orders containing it, including products that have never been ordered.
42. Display customer name, product name, quantity, and order status.

# Level 5 — JOIN + GROUP BY

43. Count the number of orders made by each customer.
44. Find the total quantity of products ordered by each customer.
45. Find the total number of units sold for each product.
46. Find the total number of orders for each order status.
47. Find the total value of each order.
   Hint: quantity * price
48. Find how much each customer has spent.
49. Find the top 5 customers by total spending.
50. Find the most ordered product by total quantity.
51. Find the average order value.
52. Find the total sales for each product category.

# Level 6 — Challenging

53. Find customers who have never placed an order.
54. Find products that have never been ordered.
55. Find the customer who has spent the most money.
56. Find the second most expensive product.
57. Find customers who have placed more than 1 order.
58. Find the product with the highest total quantity sold.
59. Find the city whose customers have spent the most money.
60. Find the most expensive order.
61. Find customers who have ordered 'Laptop'.
62. Find customers who have ordered both 'Laptop' and 'Mechanical Keyboard'.
63. Find the most popular product category based on total quantity sold.
64. Find each customer's most recent order.
65. Find customers whose total spending is greater than the average customer spending.
66. Find products whose price is greater than the average product price.
67. Find the customer with the highest number of orders.
68. Find the total revenue from only Delivered orders.
69. Find the percentage of orders that were Cancelled.
70. Create a report showing:
    customer name | order_id | product name | quantity | price | total item cost | order status

---

## Rules for Practice

Try to solve Levels 1–4 using only what you have learned so far.

For Levels 5–6, you may encounter concepts you have not learned yet. That's intentional.

Do NOT look for solutions immediately. Write your SQL query first and test it in SQLite.

