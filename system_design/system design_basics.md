# **System Design Basics**
***

## **Key Characteristics of Distributed Systems**

### **Scalability**

Scalability is the capability of a system, process, or network to grow and manage increased demand. Any distributed system that can continously evolve in order to support growing amount of work is considered to be scalable.

Reasons that a system needs to scale: increased data volume, increased amount of work like number of transactions being processed. The main mission is to acheive a level of scaling without performance loss.

Overall, a system's performance will degrade, even if it was designed to scale, with the system size due to management and environment cost. i.e network speed will be slower because machines tend to be far apart from each other, some tasks might not be distributed due to a flaw in the design. At some point these tasks will limit the speed up obtained by the architecture. Ideally, a scalable architecture avoids this situation and attempts to balance the workload on all participating nodes.


#### **Horizontal Scaling vs Vertical Scaling**

Horizontal Scaling means that you can scale by adding more servers into your pool of resources. 
Vertical Scaling means that you can scale by adding more power(CPU, RAM, storage, etc) to an existing server.

Horizontal Scaling is often easier to scale dynamically by adding more machines into the existing pool.
i.e Cassandra and MongoDB both provide an easy way to scale horizontally by adding more machines to meet growing needs.

Vertical Scaling is usually limited to the capacity of a single server and scaling beyond that capacity often involves downtime and comes with an upper limit.
i.e MySql allows for easy way to scale vertically by switching from smaller to larger machines. HOWEVER, this process often involves downtime

### **Reliability**

Reliability is the probability a system will fail in a given period. A system is deemed reliable if it keeps delivering its services even when one or several of its software or hardware components fail. 

Reliability represents one of the main characteristics of any distributed system because any failing machine can be replaced by another healthy one, ensuring the completion of the requested task.

i.e Amazon's system ensures user transactions will never be cancelled due to the failure of the machine running the transaction. For instance, if a user adds an item to his cart, the system is expected to never lose it. 
A reliable distributed system acheives this through redundancy of both the software components and data. If the server carrying the user's shopping cart fails, another server that has the exact replica of the shopping cart should replace it.

Redundancy has a cost and a reliable system has to pay that to acheive resilience for services by eliminating every single point of failure. 

### **Availability**

Availability is the time a system remains operational to perform its required function in a specific period. It is a measure of the percentage of time that a system, service, or a machine remains operational under normal conditions.
Availability is comprised of maintainability, repair time, spares availability, and other logistical considerations. Reliability is availability over time considering the full range of possible real world conditions that can occur. 

#### **Reliability vs Availability**

If a system is reliable, it is available. However, if it is available it does not necessarily mean it is reliable. In other words, high reliability contributes to high availability, but it is possible to acheive a high availability even with an unreliable product by minimizing repair time and ensuring that spares are always available when they are needed. 
i.e A system has 99.99% availability for the first two years. However the system is unreliable due to security vulnerabilities. The system gets hacked and its users data is stolen. This results in reputational and financial damage to the users.

### **Efficiency**

To measure efficiency in a distributed system, lets assume we have an operation that runs in a distributed manner and delivers a set of items as a result. Two standard measures of its efficiency are the response time (or latency) that denotes the delay to obtain the first item and throughout (or bandwidth) which denotes the number of items delivered in a given time unit (seconds). 

Two measures correspond the following unit costs: 
1. Number of messages globally sent by the nodes of the system, regardless of the message size.
2. Size of the messages representing the volume of data exchanges.

The complexity of operations supported by distributed data structures can be characterized as a function of these cost units. Keep in mind that factors like "number of messages" are over simplistic because it ignores many factors like network topology, network load, etc. However it is difficult to develop a cost model accounting all these factors, so we proceed with rough estimates of the system behavior. 

### **Serviceability or Manageability**

Serviceability or manageability is the simplicity and speed at which a system can be repaired or maintained; if the time to fix a failed system increase then the availability decreases. Things to consider for manageability are the ease of diagnosing and understanding problems when they occur, ease of making updates or modifications, and how simple is to operate. 
Early detection of faults can decrease or avoid system downtime. i.e some enterprise systems can automatically call a service center (without human intervention) when the system experiences a system fault.


## **Load Balancing**
***

Load Balancers are a critical component of any distributed system. It helps spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. LB keeps track of the status of all the resources while distributing requests. 
If a server is not available to take new requests, is not responding, or has elevated error rate, then the LB will stop sending traffic to such a server.

The LB sits between the client and the server accepting incoming network, application traffic, and distributing the traffic across multiple backend servers using various algorithms. 

By balancing application requests across multiple servers, a load balancer reduces individual server load and prevents any one application server from becoming a single point of failure, thus improving overall application availability and responsiveness.
![alt text](https://github.com/chunisama/leetcode/blob/master/system_design/load_balancer.png)

To utilize full scalability and redundancy, we can try to balance the load at each layer of the system. We can add Lbs at three places.
1. Between the user and the web server.
2. Between web servers and an internal platform layer, like application servers or cache servers.
3. Between the internal platform layer and database.
   
![alt text](https://github.com/chunisama/leetcode/blob/master/system_design/load_balancer_locations.png)

### **Benefits of Load Balancers**

* Users experience faster, uninterrupted service. Users wont need to wait on a struggling server to finish its previous tasks. Instead their requests are passed to a more readily available resource. 
* Service providers experience less downtime and higher throughput. Even a full server failure won't affect the end user experience as the load balancer will route around it to a healthy server.
* Load balancing makes it easier for system administrators to handle incoming requests while decreasing user wait time.
* Smart load balancers provide benefits like predictive analytics that determine traffic bottlenecks before they happen. As a result, smart load balancers provide organized actionable insights. These are vital for automation and can drive business decisions.
* System administrators experience fewer failed/stressed components. Instead of a single device performing a lot of work, load balancing has several devices do a little work. 

### **Load Balancing Algorithms**

A Load Balancer considers two factors before forwarding a request to a backend server.
1. Ensure that the server is actually responding appropriately to requests.
2. Use a pre-configured algorithm to select one from the pool of healthy servers.

Load balancers shouly only forward requests to healthy backend servers. Health Checks ensure if the server is actually responding appropriately. Basically, health checks regularly attempt to connect to the backend servers to ensure that servers are listening. If a server fails a health check, it is automatically removed from the pool and traffic will not be forwarded to it until it responds to health checks again.

There are a variety of load balancing methods, which use different algorithms for different needs.

* Least Connection Method: This method directs traffic to the server with fewest active connections. This approach is useful when there are a large number of persistent client connections, which are unevenly distributed between the servers.
* Least Response Time Method: This algorithm directs traffic to the server with the fewest active connections and the lowest average response time. 
* Least Bandwidth Method: This method selects the server that is currently serving the least amount of traffic measured in megabits per second (Mbps).
* Round Robin Method: This method cycles through a list of servers and sends each new request to the next server. When it reaches the end of the list, it starts over at the beginning. It is most useful when the servers are of equal speci cation and there are not many persistent connections.
* Weighted Round Robin Method: The weighted round-robin scheduling is designed to better handle servers with different processing capacities. Each server is assigned a weight (an integer value that indicates the processing capacity). Servers with higher weights receive new connections before those with less weights and servers with higher weights get more connections than those with less weights.
* IP Hash: Under this method, a hash of the IP address of the client is calculated to redirect the request to a server.

### **Redundant Load Balancers**

The Load Balancer can be a single point of failure; to ovecome this, a second load alancer can be connected to the first to form a cluster. Each LB monitors the health of the other and, since both of them are equally capable of serving traffic and failure detection, in the event the main load balancer fails, the second load balancer takes over.

