DevOps Whist Project
Description
This project demonstrates a simple web application setup using Docker Compose. The application consists of three Python Flask applications, a MySQL database, and an Nginx load balancer. The applications log access details and maintain a global counter. The Nginx load balancer distributes traffic between the applications and provides sticky session functionality.

Components
app1, app2, app3: Python Flask applications.
db: MySQL database container.
nginx: Nginx load balancer container.
Endpoints
/: Access the applications (switches between app1, app2, and app3).
/showcount: Display the global counter value.
Prerequisites
Docker
Docker Compose
Setup
Clone the repository:

sh
Copy code
git clone https://github.com/Zeavan23/DevOps-W.git
cd DevOps-W
Build and start the containers:

sh
Copy code
docker-compose up --build
Access the application and showcount endpoint:

http://localhost/
http://localhost/showcount
Scaling
To scale the application containers to 5 instances, run:

sh
Copy code
./scale.sh
License
This project is licensed under the MIT License.
