# DMS-Migration

Migrating an on-premises MySQL database to Amazon RDS MySQL by using AWS Database Migration Services (DMS).After the migration is completed, we are invoking a Lambda function. That Lambda function checks and retrieves the newly added records from the RDS MySQL Database and inserts them into the AWS DynamoDB Database.

**AWS Services :** AWS RDS, AWS DMS, Lambda Function, AWS DynamoDB, CloudWatch, VPC 


# Project Description : 

### 1. Create on-premises MySQL
Set up an on-premises MySQL database using MySQL Workbench. Create a table named **EmployeeDetails** within this database, and then insert few records into the table.

### 2. Create RDS MySQL
Create RDS MySQL Database called **awsemployeedb** in AWS as the target Database.And create a Security Group named **mysql-sg** and make sure the port “3360” is open in the inbound rule, set it if not open and attach to the database.

<img src="https://github.com/user-attachments/assets/19d6e4df-8a93-4821-8f60-d09e5fceba91">

### 3. Create Replication Instance
Create a Replication Instance called **dbreplica** to handle data migration.And also you need to check whether your security group allows your replication instance to access your database or not.For that go to the security group remove the existing “IP address” and enter the “name of the security group” used for your Amazon RDS database instance and replication instance.

<img src="https://github.com/user-attachments/assets/700a9bce-7016-43ad-b06d-d8bfd7866a82" width="400px">

### 4. Create Source and Target endpoints
Set up Source and Target endpoints in AWS DMS called **onpremisemysql** and **awsemployeemysql** for the on-premises MySQL and RDS MySQL databases. After creating these endpoint, make sure to test the connection before migrating.

<img src="https://github.com/user-attachments/assets/55f9c2b2-9f59-41fe-bbdd-b4c742815d89">

### 5. Create Migration Task
Create and Configure a Migration task in DMS called **migrationdb** to transfer data from the on-premises database to the RDS instance.Execute the migration task and monitor its progress through the AWS DMS console.

<img src="https://github.com/user-attachments/assets/c89959a2-96ee-447d-a44d-d72e48b5db98"><img src="https://github.com/user-attachments/assets/0c84d26f-6c40-4a88-964b-36b65562def4">

### 6. Migration Task Output
Once the Migration is completed connect to the RDS database using MySQL Workbench to check the migrated data.Execute queries in MySQL Workbench to ensure that records in EmployeeDetails are correctly migrated.

### 7. Create Lambda Function
After the migration is completed, a Lambda Function will be triggered to query and fetch all the new records from the RDS Mysql database.It will then insert these records one by one into DynamoDB.Attach a permission to the Lambda function to access DynamoDB.
   
### 8. Create DynamoDB
AWS DynamoDB is a fully managed, serverless, NoSQL database service provided by AWS.Access the DynamoDB console and navigate to the table named **employeedb**. Monitor the table to verify that all records have been properly added to the database or not.

<img src="https://github.com/user-attachments/assets/c8bc0a95-c277-4a81-8bf1-15dcea4543b9">



