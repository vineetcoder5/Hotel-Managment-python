# Hotel-Managment-python
"Python-based Hotel Management System: Handles room reservations, check-ins, checkouts, and employee management using MySQL database. Efficient and easy-to-use application."



The Hotel Management System is a command-line based application designed to handle hotel room bookings, check-ins, and checkouts. Employees and staff can use the system to manage customer reservations and room status efficiently. Here are the key features of the system:

Room Management:
The system allows employees to add new rooms to the hotel's database, specifying room numbers and categories (e.g., single, double, deluxe).

Room Availability Check:
Employees can check the availability of rooms based on customer preferences, such as room category. The system queries the database to retrieve the available rooms and displays them to the user.

Customer Check-In:
Employees can assist customers in checking in to available rooms. The system records customer details, including name, phone number, adhar card number, and the checkout date.

Customer Check-Out:
Upon check-out, employees can mark a room as available and update the checkout date for the customer's record.

Employee Management:
The system allows administrators to add new employees to the database, including their names, phone numbers, and login codes.

Data Retrieval:
The system offers options to retrieve customer and employee data. Employees can search for specific customer records or view the entire list of customers. Additionally, they can view details of all employees or search for specific employee records.

Revenue Tracking (Partial Implementation):
The code contains a feature to calculate revenue by counting the number of customers who have not checked out (i.e., are still occupying the room).
