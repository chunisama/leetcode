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

* **Least Connection Method**: This method directs traffic to the server with fewest active connections. This approach is useful when there are a large number of persistent client connections, which are unevenly distributed between the servers.
* **Least Response Time Method**: This algorithm directs traffic to the server with the fewest active connections and the lowest average response time. 
* **Least Bandwidth Method**: This method selects the server that is currently serving the least amount of traffic measured in megabits per second (Mbps).
* **Round Robin Method**: This method cycles through a list of servers and sends each new request to the next server. When it reaches the end of the list, it starts over at the beginning. It is most useful when the servers are of equal speci cation and there are not many persistent connections.
* **Weighted Round Robin Method**: The weighted round-robin scheduling is designed to better handle servers with different processing capacities. Each server is assigned a weight (an integer value that indicates the processing capacity). Servers with higher weights receive new connections before those with less weights and servers with higher weights get more connections than those with less weights.
* **IP Hash**: Under this method, a hash of the IP address of the client is calculated to redirect the request to a server.

### **Redundant Load Balancers**

The Load Balancer can be a single point of failure; to ovecome this, a second load alancer can be connected to the first to form a cluster. Each LB monitors the health of the other and, since both of them are equally capable of serving traffic and failure detection, in the event the main load balancer fails, the second load balancer takes over.

![alt text](https://github.com/chunisama/leetcode/blob/master/system_design/redundant%20LB.png)

## **Caching**
**

Load balancing helps you scale horizontally across an ever-increasing number of servers, but caching will enable you to make vastly better use of the resources you already have as well as making otherwise unattainable product requirements feasible. Caches take advantage of the locality of reference principle: recently requested data is likely to be requested again. They are used in almost every layer of computing: hardware, operating systems, web browsers, web applications, and more. A cache is like short- term memory: it has a limited amount of space, but is typically faster than the original data source and contains the most recently accessed items.

Caches can exist at all levels in architecture, but are often found at the level nearest to the front end where they are implemented to return data quickly without taxing downstream levels.

### **Application Server Cache**

Placing a cache directly on a request layer node enables the local storage of response data. Each time a request is made to the service, the node will quickly return local cached data if it exists. If it is not in the cache, the requesting node will query the data from disk. The cache on one request layer node could also be located both in memory (which is very fast) and on the node’s local disk (faster than going to network storage).
What happens when you expand this to many nodes? If the request layer is expanded to multiple nodes, it’s still quite possible to have each node host its own cache. However, if your load balancer randomly distributes requests across the nodes, the same request will go to different nodes, thus increasing cache misses. Two choices for overcoming this hurdle are global caches and distributed caches.

### **Content Distribution Network**

CDNs are a kind of cache that comes into play for sites serving large amounts of static media. In a typical CDN setup, a request will first ask the CDN for a piece of static media; the CDN will serve that content if it has it locally available. If it isn’t available, the CDN will query the back-end servers for the file, cache it locally, and serve it to the requesting user.
If the system we are building isn’t yet large enough to have its own CDN, we can ease a future transition by serving the static media off a separate subdomain (e.g. static.yourservice.com) using a lightweight HTTP server like Nginx, and cut-over the DNS from your servers to a CDN later.

### **Cache Invalidation**

While caching is fantastic, it does require some maintenance for keeping cache coherent with the source of truth (e.g., database). If the data is modified in the database, it should be invalidated in the cache; if not, this can cause inconsistent application behavior.
Solving this problem is known as cache invalidation; there are three main schemes that are used:

#### **Write-Through Cache**

Under this scheme, data is written into the cache and the corresponding database at the same time. The cached data allows for fast retrieval and, since the same data gets written in the permanent storage, we will have complete data consistency between the cache and the storage. Also, this scheme ensures that nothing will get lost in case of a crash, power failure, or other system disruptions.
Although, write through minimizes the risk of data loss, since every write operation must be done twice before returning success to the client, this scheme has the disadvantage of higher latency for write operations.

#### **Write-Around Cache**

This technique is similar to write through cache, but data is written directly to permanent storage, bypassing the cache. This can reduce the cache being flooded with write operations that will not subsequently be re-read, but has the disadvantage that a read request for recently written data will create a “cache miss” and must be read from slower back-end storage and experience higher latency.

#### **Write-Back Cache**

Under this scheme, data is written to cache alone and completion is immediately con rmed to the client. The write to the permanent storage is done after speci ed intervals or under certain conditions. This results in low latency and high throughput for write-intensive applications, however, this speed comes with the risk of data loss in case of a crash or other adverse event because the only copy of the written data is in the cache.

#### **Cache-Eviction Policies**

Following are some of the most common cache eviction policies:
1. **First In First Out (FIFO)**: The cache evicts the first block accessed first without any regard to how often or how many times it was accessed before.
2. **Last In First Out (LIFO)**: The cache evicts the block accessed most recently first without any regard to how often or how many times it was accessed before.
3. **Least Recently Used (LRU)**: Discards the least recently used items first.
4. **Most Recently Used (MRU)**: Discards, in contrast to LRU, the most recently used items first.
5. **Least Frequently Used (LFU)**: Counts how often an item is needed. Those that are used least often are discarded first.
6. **Random Replacement (RR)**: Randomly selects a candidate item and discards it to make space when necessary.

## **Sharding or Data Partitioning**
***

Data partitioning (also known as sharding) is a technique to break up a big database (DB) into many smaller parts. It is the process of splitting up a DB/table across multiple machines to improve the manageability, performance, availability, and load balancing of an application. The justi cation for data sharding is that, after a certain scale point, it is cheaper and more feasible to scale horizontally by adding more machines than to grow it vertically by adding bee er servers.

### **1. Partitioning Methods**

There are many different schemes one could use to decide how to break up an application database into multiple smaller DBs. Below are three of the most popular schemes used by various large scale applications.

a. **Horizontal partitioning**: In this scheme, we put different rows into different tables. For example, if we are storing different places in a table, we can decide that locations with ZIP codes less than 10000 are stored in one table and places with ZIP codes greater than 10000 are stored in a separate table. This is also called a range based sharding as we are storing different ranges of data in separate tables.
The key problem with this approach is that if the value whose range is used for sharding isn’t chosen carefully, then the partitioning scheme will lead to unbalanced servers. In the previous example, splitting location based on their zip codes assumes that places will be evenly distributed across the different zip codes. This assumption is not valid as there will be a lot of places in a thickly populated area like Manhattan as compared to its suburb cities.

b. **Vertical Partitioning**: In this scheme, we divide our data to store tables related to a specific feature in their own server. For example, if we are building Instagram like application - where we need to store data related to users, photos they upload, and people they follow - we can decide to place user profile information on one DB server, friend lists on another, and photos on a third server. Vertical partitioning is straightforward to implement and has a low impact on the application. The main problem with this approach is that if our application experiences additional growth, then it may be necessary to further partition a feature specific DB across various servers (e.g. it would not be possible for a single server to handle all the metadata queries for 10 billion photos by 140 million users).

c. **Directory Based Partitioning**: A loosely coupled approach to work around issues mentioned in the above schemes is to create a lookup service which knows your current partitioning scheme and abstracts it away from the DB access code. So, to find out where a particular data entity resides, we query the directory server that holds the mapping between each tuple key to its DB server. This loosely coupled approach means we can perform tasks like adding servers to the DB pool or changing our partitioning scheme without having an impact on the application.

### **2. Partitioning Criteria**

a. **Key or Hash-based partitioning**: Under this scheme, we apply a hash function to some key attributes of the entity we are storing; that yields the partition number. For example, if we have 100 DB servers and our ID is a numeric value that gets incremented by one each time a new record is inserted. In this example, the hash function could be ‘ID % 100’, which will give us the server number where we can store/read that record. This approach should ensure a uniform allocation of data among servers. The fundamental problem with this approach is that it effectively fixes the total number of DB servers, since adding new servers means changing the hash function which would require redistribution of data and downtime for the service. A workaround for this problem is to use Consistent Hashing.

b. **List partitioning**: In this scheme, each partition is assigned a list of values, so whenever we want to insert a new record, we will see which partition contains our key and then store it there. For example, we can decide all users living in Iceland, Norway, Sweden, Finland, or Denmark will be stored in a partition for the Nordic countries.

c. **Round-robin partitioning**: This is a very simple strategy that ensures uniform data distribution. With ‘n’ partitions, the ‘i’ tuple is assigned to partition (i mod n).

d. **Composite partitioning**: Under this scheme, we combine any of the above partitioning schemes to devise a new scheme. For example, first applying a list partitioning scheme and then a hash based partitioning. Consistent hashing could be considered a composite of hash and list partitioning where the hash reduces the key space to a size that can be listed.

### **3. Common Problems of Sharding**

On a sharded database there are certain extra constraints on the different operations that can be performed. Most of these constraints are due to the fact that operations across multiple tables or multiple rows in the same table will no longer run on the same server. Below are some of the constraints and additional complexities introduced by sharding:

a. **Joins and Denormalization**: Performing joins on a database which is running on one server is straightforward, but once a database is partitioned and spread across multiple machines it is often not feasible to perform joins that span database shards. Such joins will not be performance efficient since data has to be compiled from multiple servers. A common workaround for this problem is to denormalize the database so that queries that previously required joins can be performed from a single table. Of course, the service now has to deal with all the perils of denormalization such as data inconsistency.

b. **Referential integrity**: As we saw that performing a cross-shard query on a partitioned database is not feasible, similarly, trying to enforce data integrity constraints such as foreign keys in a sharded database can be extremely diffcult. Most of RDBMS do not support foreign keys constraints across databases on different database servers. Which means that applications that require referential integrity on sharded databases often have to enforce it in application code. Often in such cases, applications have to run regular SQL jobs to clean up dangling references.

c. **Rebalancing**: There could be many reasons we have to change our sharding scheme:
1. The data distribution is not uniform, e.g., there are a lot of places for a particular ZIP code that cannot fit into one database partition.
2. There is a lot of load on a shard, e.g., there are too many requests being handled by the DB shard dedicated to user photos.
In such cases, either we have to create more DB shards or have to rebalance existing shards, which means the partitioning scheme changed and all
existing data moved to new locations. Doing this without incurring downtime is extremely di cult. Using a scheme like directory based partitioning does make rebalancing a more palatable experience at the cost of increasing the complexity of the system and creating a new single point of failure (i.e. the lookup service/database).

## **Indexes**
**

Indexes are well known when it comes to databases. Sooner or later there comes a time when database performance is no longer satisfactory. One of the very first things you should turn to when that happens is database indexing.
The goal of creating an index on a particular table in a database is to make it faster to search through the table and find the row or rows that we want. Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.

Example: A library catalog
A library catalog is a register that contains the list of books found in a library. The catalog is organized like a database table generally with four columns: book title, writer, subject, and date of publication. There are usually two such catalogs: one sorted by the book title and one sorted by the writer name. That way, you can either think of a writer you want to read and then look through their books or look up a specific book title you know you want to read in case you don’t know the writer’s name. These catalogs are like indexes for the database of books. They provide a sorted list of data that is easily searchable by relevant information.
Simply saying, an index is a data structure that can be perceived as a table of contents that points us to the location where actual data lives. So when we create an index on a column of a table, we store that column and a pointer to the whole row in the index.

How do Indexes decrease write performance?
An index can dramatically speed up data retrieval but may itself be large due to the additional keys, which slow down data insertion & update.
When adding rows or making updates to existing rows for a table with an active index, we not only have to write the data but also have to update the index. This will decrease the write performance. This performance degradation applies to all insert, update, and delete operations for the table. For this reason, adding unnecessary indexes on tables should be avoided and indexes that are no longer used should be removed. To reiterate, adding indexes is about improving the performance of search queries. If the goal of the database is to provide a data store that is often written to and rarely read from, in that case, decreasing the performance of the more common operation, which is writing, is probably not worth the increase in performance we get from reading.

## **Proxies**
**

A proxy server is an intermediate server between the client and the back-end server. Clients connect to proxy servers to request for a service like a web page, file, connection, etc. In short, a proxy server is a piece of software or hardware that acts as an intermediary for requests from clients seeking resources from other servers.
Typically, proxies are used to filter requests, log requests, or sometimes transform requests (by adding/removing headers, encrypting/decrypting, or compressing a resource). Another advantage of a proxy server is that its cache can serve a lot of requests. If multiple clients access a particular resource, the proxy server can cache it and serve it to all the clients without going to the remote server.

![alt text](https://github.com/chunisama/leetcode/blob/master/system_design/proxy%20server.png)


### **Proxy Server Types**

Proxies can reside on the client’s local server or anywhere between the client and the remote servers. Here are a few famous types of proxy servers:

#### **Open Proxy**

An open proxy is a proxy server that is accessible by any Internet user. Generally, a proxy server only allows users within a network group (i.e. a closed proxy) to store and forward Internet services such as DNS or web pages to reduce and control the bandwidth used by the group. With an open proxy, however, any user on the Internet is able to use this forwarding service. There two famous open proxy types:
1. Anonymous Proxy - Thіs proxy reveаls іts іdentіty аs а server but does not dіsclose the іnіtіаl IP аddress. Though thіs proxy server cаn be dіscovered eаsіly іt cаn be benefіcіаl for some users аs іt hіdes their IP аddress.
2. Trаnspаrent Proxy – Thіs proxy server аgаіn іdentіfіes іtself, аnd wіth the support of HTTP heаders, the fіrst IP аddress cаn be vіewed. The mаіn benefіt of usіng thіs sort of server іs іts аbіlіty to cаche the websіtes.
   
#### **Reverse Proxy**
A reverse proxy retrieves resources on behalf of a client from one or more servers. These resources are then returned to the client, appearing as if they originated from the proxy server itself.

## **Redundancy and Replication**
**

Redundancy is the duplication of critical components or functions of a system with the intention of increasing the reliability of the system, usually in the form of a backup or fail-safe, or to improve actual system performance. For example, if there is only one copy of a file stored on a single server, then losing that server means losing the file. Since losing data is seldom a good thing, we can create duplicate or redundant copies of the file to solve this problem.
Redundancy plays a key role in removing the single points of failure in the system and provides backups if needed in a crisis. For example, if we have two instances of a service running in production and one fails, the system can failover to the other one.
Replication means sharing information to ensure consistency between redundant resources, such as software or hardware components, to improve reliability, fault-tolerance, or accessibility.
Replication is widely used in many database management systems (DBMS), usually with a master-slave relationship between the original and the copies. The master gets all the updates, which then ripple through to the slaves. Each slave outputs a message stating that it has received the update successfully, thus allowing the sending of subsequent updates.

## **SQL vs NoSQL**
**

In the world of databases, there are two main types of solutions: SQL and NoSQL (or relational databases and non-relational databases). Both of them differ in the way they were built, the kind of information they store, and the storage method they use.
Relational databases are structured and have predefined schemas like phone books that store phone numbers and addresses. Non-relational databases are unstructured, distributed, and have a dynamic schema like file folders that hold everything from a person’s address and phone number to their Facebook ‘likes’ and online shopping preferences.

### **SQL**

Relational databases store data in rows and columns. Each row contains all the information about one entity and each column contains all the separate data points. Some of the most popular relational databases are MySQL, Oracle, MS SQL Server, SQLite, Postgres, and MariaDB.

### **NoSQL**

Following are the most common types of NoSQL:
**Key-Value Stores**: Data is stored in an array of key-value pairs. The ‘key’ is an
attribute name which is linked to a ‘value’. Well-known key-value stores include Redis, Voldemort, and Dynamo.
 
**Document Databases**: In these databases, data is stored in documents (instead of rows and columns in a table) and these documents are grouped together in collections. Each document can have an entirely di erent structure. Document databases include the CouchDB and MongoDB. 
Wide-Column Databases: Instead of ‘tables,’ in columnar databases we have column families, which are containers for rows. Unlike relational databases, we don’t need to know all the columns up front and each row doesn’t have to have the same number of columns. Columnar databases are best suited for analyzing large datasets - big names include Cassandra and HBase.

**Graph Databases:** These databases are used to store data whose relations are best represented in a graph. Data is saved in graph structures with nodes (entities), properties (information about the entities), and lines (connections between the entities). Examples of graph database include Neo4J and InfiniteGraph.

### **High Level Differences Between SQL and NoSQL**

**Storage**: SQL stores data in tables where each row represents an entity and each column represents a data point about that entity; for example, if we are storing a car entity in a table, different columns could be ‘Color’, ‘Make’, ‘Model’, and so on.

NoSQL databases have different data storage models. The main ones are key-value, document, graph, and columnar. We will discuss differences between these databases below.

**Querying**: SQL databases use SQL (structured query language) for defining and manipulating the data, which is very powerful. In a NoSQL database, queries are focused on a collection of documents. Sometimes it is also called UnQL (Unstructured Query Language). Different databases have different syntax for using UnQL.

**Scalability**: In most common situations, SQL databases are vertically scalable, i.e., by increasing the horsepower (higher Memory, CPU, etc.) of the hardware, which can get very expensive. It is possible to scale a relational database across multiple servers, but this is a challenging and time-consuming process.

On the other hand, NoSQL databases are horizontally scalable, meaning we can add more servers easily in our NoSQL database infrastructure to handle a lot of traffic. Any cheap commodity hardware or cloud instances can host NoSQL databases, thus making it a lot more cost-effective than vertical scaling. A lot of NoSQL technologies also distribute data across servers automatically.

**Reliability or ACID Compliancy (Atomicity, Consistency, Isolation, Durability)**: The vast majority of relational databases are ACID compliant. So, when it comes to data reliability and safe guarantee of performing transactions, SQL databases are still the better bet.

Most of the NoSQL solutions sacrifice ACID compliance for performance and scalability.

### **SQL VS. NoSQL - Which one to use?**

When it comes to database technology, there’s no one-size-fits-all solution. That’s why many businesses rely on both relational and non-relational databases for different needs. Even as NoSQL databases are gaining popularity for their speed and scalability, there are still situations where a highly structured SQL database may perform better; choosing the right technology hinges on the use case.

#### **Reasons to use SQL database**

Here are a few reasons to choose a SQL database:

1. We need to ensure ACID compliance. ACID compliance reduces anomalies and protects the integrity of your database by prescribing exactly how transactions interact with the database. Generally, NoSQL databases sacrifice ACID compliance for scalability and processing speed, but for many e-commerce and financial applications, an ACID-compliant database remains the preferred option.
   
2. Your data is structured and unchanging. If your business is not experiencing massive growth that would require more servers and if you’re only working with data that is consistent, then there may be no reason to use a system designed to support a variety of data types and high traffic volume.

#### **Reasons to use NoSQL database**

When all the other components of our application are fast and seamless, NoSQL databases prevent data from being the bottleneck. Big data is contributing to a large success for NoSQL databases, mainly because it handles data differently than the traditional relational databases. A few popular examples of NoSQL databases are MongoDB, CouchDB, Cassandra, and HBase.

1. Storing large volumes of data that often have little to no structure. A NoSQL database sets no limits on the types of data we can store together and allows us to add new types as the need changes. With document-based databases, you can store data in one place without having to define what “types” of data those are in advance.

2. Making the most of cloud computing and storage. Cloud-based storage is an excellent cost-saving solution but requires data to be easily spread across multiple servers to scale up. Using commodity (affordable, smaller) hardware on-site or in the cloud saves you the hassle of additional software and NoSQL databases like Cassandra are designed to be scaled across multiple data centers out of the box, without a lot of headaches.

3. Rapid development. NoSQL is extremely useful for rapid development as it doesn’t need to be prepped ahead of time. If you’re working on quick iterations of your system which require making frequent updates to the data structure without a lot of downtime between versions, a relational database will slow you down.

## **CAP Theorem**
**

CAP theorem states that it is impossible for a distributed software system to simultaneously provide more than two out of three of the following guarantees (CAP): Consistency, Availability, and Partition tolerance. When we design a distributed system, trading off among CAP is almost the first thing we want to consider. CAP theorem says while designing a distributed system we can pick only two of the following three options:

**Consistency**: All nodes see the same data at the same time. Consistency is achieved by updating several nodes before allowing further reads.

**Availability**: Every request gets a response on success/failure. Availability is achieved by replicating the data across different servers.

**Partition tolerance**: The system continues to work despite message loss or partial failure. A system that is partition-tolerant can sustain any amount of network failure that doesn’t result in a failure of the entire network. Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.

We cannot build a general data store that is continually available, sequentially consistent, and tolerant to any partition failures. We can only build a system that has any two of these three properties. Because, to be consistent, all nodes should see the same set of updates in the same order. But if the network suffers a partition, updates in one partition might not make it to the other partitions before a client reads from the out-of-date partition after having read from the up-to-date one. The only thing that can be done to cope with this possibility is to stop serving requests from the out-of-date partition, but then the service is no longer 100% available.

## **Consistent Hashing**

Distributed Hash Table (DHT) is one of the fundamental components used in distributed scalable systems. Hash Tables need a key, a value, and a hash function where hash function maps the key to a location where the value is stored.

**index = hash_function(key)**

Suppose we are designing a distributed caching system. Given ‘n’ cache servers, an intuitive hash function would be ‘key % n’. It is simple and commonly used. But it has two major drawbacks:

1. It is NOT horizontally scalable. Whenever a new cache host is added to the system, all existing mappings are broken. It will be a pain point in maintenance if the caching system contains lots of data. Practically, it becomes difficult to schedule a downtime to update all caching mappings.

2. It may NOT be load balanced, especially for non-uniformly distributed data. In practice, it can be easily assumed that the data will not be distributed uniformly. For the caching system, it translates into some caches becoming hot and saturated while the others idle and are almost empty.
In such situations, consistent hashing is a good way to improve the caching system.

### **What is Consistent Hashing?**

Consistent hashing is a very useful strategy for distributed caching system and DHTs. It allows us to distribute data across a cluster in such a way that will minimize reorganization when nodes are added or removed. Hence, the caching system will be easier to scale up or scale down.

In Consistent Hashing, when the hash table is resized (e.g. a new cache host is added to the system), only ‘k/n’ keys need to be remapped where ‘k’ is the total number of keys and ‘n’ is the total number of servers. Recall that in a caching system using the ‘mod’ as the hash function, all keys need to be remapped.

In Consistent Hashing, objects are mapped to the same host if possible. When a host is removed from the system, the objects on that host are shared by other hosts; when a new host is added, it takes its share from a few hosts without touching other’s shares.

### **How does it work?**

As a typical hash function, consistent hashing maps a key to an integer. Suppose the output of the hash function is in the range of [0, 256). Imagine that the integers in the range are placed on a ring such that the values are wrapped around.

Here’s how consistent hashing works:

1. Given a list of cache servers, hash them to integers in the range.
2. To map a key to a server,
    * Hash it to a single integer.
    * Move clockwise on the ring until finding the first cache it encounters.
    * That cache is the one that contains the key. See animation below as an example: key1 maps to cache A; key2 maps to cache C.

To add a new server, say D, keys that were originally residing at C will be split. Some of them will be shifted to D, while other keys will not be touched.

To remove a cache or, if a cache fails, say A, all keys that were originally mapped to A will fall into B, and only those keys need to be moved to B; other keys will not be affected.

For load balancing, as we discussed in the beginning, the real data is essentially randomly distributed and thus may not be uniform. It may make the keys on caches unbalanced.

To handle this issue, we add “virtual replicas” for caches. Instead of mapping each cache to a single point on the ring, we map it to multiple points on the ring, i.e. replicas. This way, each cache is associated with multiple portions of the ring.

If the hash function “mixes well,” as the number of replicas increases, the keys will be more balanced.

## **Long-Polling vs WebSockets vs Server-Sent Events**
##

Long-Polling, WebSockets, and Server-Sent Events are popular communication protocols between a client like a web browser and a web server. First, let’s start with understanding what a standard HTTP web request looks like. Following are a sequence of events for regular HTTP request:

1. The client opens a connection and requests data from the server.
2. The server calculates the response.
3. The server sends the response back to the client on the opened request.

### **Ajax Polling**

Polling is a standard technique used by the vast majority of AJAX applications. The basic idea is that the client repeatedly polls (or requests) a server for data. The client makes a request and waits for the server to respond with data. If no data is available, an empty response is returned.

1. The client opens a connection and requests data from the server using regular HTTP.
2. The requested webpage sends requests to the server at regular intervals (e.g., 0.5 seconds).
3. The server calculates the response and sends it back, just like regular HTTP traffic.
4. The client repeats the above three steps periodically to get updates from the server.

The problem with Polling is that the client has to keep asking the server for any new data. As a result, a lot of responses are empty, creating HTTP overhead.

### **HTTP Long-Polling**

This is a variation of the traditional polling technique that allows the server to push information to a client whenever the data is available. With Long-Polling, the client requests information from the server exactly as in normal polling, but with the expectation that the server may not respond immediately. That’s why this technique is sometimes referred to as a “Hanging GET”.

* If the server does not have any data available for the client, instead of sending an empty response, the server holds the request and waits until some data becomes available.
* Once the data becomes available, a full response is sent to the client. The client then immediately re-request information from the server so that the server will almost always have an available waiting request that it can use to deliver data in response to an event.

The basic life cycle of an application using HTTP Long-Polling is as follows:

1. The client makes an initial request using regular HTTP and then waits for a response.
2. The server delays its response until an update is available or a timeout has occurred.
3. When an update is available, the server sends a full response to the client.
4. The client typically sends a new long-poll request, either immediately upon receiving a response or after a pause to allow an acceptable latency period.
5. Each Long-Poll request has a timeout. The client has to reconnect periodically after the connection is closed due to timeouts.

### **Websockets**

WebSocket provides Full duplex communication channels over a single TCP connection. It provides a persistent connection between a client and a server that both parties can use to start sending data at any time. The client establishes a WebSocket connection through a process known as the WebSocket handshake. If the process succeeds, then the server and client can exchange data in both directions at any time. The WebSocket protocol enables communication between a client and a server with lower overheads, facilitating real-time data transfer from and to the server. This is made possible by providing a standardized way for the server to send content to the browser without being asked by the client and allowing for messages to be passed back and forth while keeping the connection open. In this way, a two-way (bi-directional) ongoing conversation can take place between a client and a server.

### **Server-Sent Events (SSEs)**

Under SSEs the client establishes a persistent and long-term connection with the server. The server uses this connection to send data to a client. If the client wants to send data to the server, it would require the use of another technology/protocol to do so.

1. Client requests data from a server using regular HTTP.
2. The requested webpage opens a connection to the server.
3. The server sends the data to the client whenever there’s new information available.

SSEs are best when we need real-time traffic from the server to the client or if the server is generating data in a loop and will be sending multiple events to the client.