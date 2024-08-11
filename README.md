# MySQL to AWS RDS Migration with DynamoDB Integration

Migrating an on-premises MySQL database to Amazon RDS MySQL by using AWS Database Migration Services (DMS).And Configured a CloudWatch Subscription filter to look for specific patterns related to new records . If the pattern matches, we are triggering a Lambda function. That Lambda function checks and retrieves the newly added records from the RDS MySQL Database and inserts them into the AWS DynamoDB Database.

<img src="https://github.com/user-attachments/assets/a83fd4e0-ebc2-4f03-b591-c79cad227aef">

### AWS Services : AWS RDS, AWS DMS, Lambda Function, AWS DynamoDB, CloudWatch, VPC


# Project Description : 

### 1. Set Up On-Premises MySQL Database
Ensure that MySQL is installed and running in your on-premises environment. Create the necessary databases and tables that you plan to migrate to Amazon RDS. Populate these tables with some initial records to serve as the source data for the migration.


### 2. Create Amazon RDS MySQL Instance
In the AWS Management Console, create an RDS MySQL instance named **awsemployeedb**. Configure the instance type, storage, and network settings. Set up a Security Group named mysql-sg with port 3306 open in the inbound rules and attach it to the instance.

<img src="https://github.com/user-attachments/assets/19d6e4df-8a93-4821-8f60-d09e5fceba91">


### 3. Create Replication Instance
Navigate to the AWS DMS Console and create a new replication instance named **dbreplica**. This instance serves as a bridge between your on-premises MySQL database and the RDS MySQL database. Select an instance size and settings that align with your workload requirements.

<img src="https://github.com/user-attachments/assets/700a9bce-7016-43ad-b06d-d8bfd7866a82">

### 4. Create Source and Target endpoints
Set up the source endpoint to connect to your on-premises MySQL database by providing the necessary connection details such as server name, port, database name, and credentials. Similarly, set up the target endpoint to connect to your RDS MySQL instance, and provide the connection details for the RDS instance.

<img src="https://github.com/user-attachments/assets/55f9c2b2-9f59-41fe-bbdd-b4c742815d89">

### 5. Create Migration Task
In the AWS DMS Console, create a new migration task to transfer data from your on-premises MySQL database to the RDS MySQL instance. Choose the appropriate migration type, specify the replication instance, and configure the source and target endpoints you created earlier. Additionally, set up table mappings to include the tables you wish to migrate. Start the migration task and monitor its status in the DMS console.

<img src="https://github.com/user-attachments/assets/c89959a2-96ee-447d-a44d-d72e48b5db98"><img src="https://github.com/user-attachments/assets/0c84d26f-6c40-4a88-964b-36b65562def4">

### 6. Configure CloudWatch Monitoring
Enable CloudWatch Logs for your RDS MySQL instance and configure a subscription filter to monitor logs for patterns indicating the addition of new records. In CloudWatch, create a subscription filter to match specific patterns, such as SQL INSERT statements.

### 7. Configure Lambda Function
In the AWS Lambda console, create a new function that is triggered by CloudWatch Logs. This function should query and fetch new records from the RDS MySQL database and insert these records into DynamoDB. Additionally, attach the necessary permissions to the Lambda function to allow access to DynamoDB.
   
### 8. Create DynamoDB Table
In the DynamoDB console, create a new table to store the migrated records. Specify the partition key schema and any required sort indexes.Monitor the table to confirm that records are correctly added and use the DynamoDB console 

<img src="https://github.com/user-attachments/assets/c8bc0a95-c277-4a81-8bf1-15dcea4543b9">



