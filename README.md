# DMS-Migration

Migrating an on-premises MySQL database to Amazon RDS MySQL by using AWS Database Migration Services (DMS).After the migration is completed, we are invoking a Lambda function. That Lambda function checks and retrieves the newly added records from the RDS MySQL Database and inserts them into AWS DynamoDB Database.

# Project Steps


1. Create Local Mysql Database and table for the source Database

2. Create RDS MySQL Database for the target Database
<img src="https://github.com/user-attachments/assets/19d6e4df-8a93-4821-8f60-d09e5fceba91" width="400px">

3. Create Replication Instance
<img src="https://github.com/user-attachments/assets/700a9bce-7016-43ad-b06d-d8bfd7866a82" width="400px">

4. Create Target and Source Endpoints
<img src="https://github.com/user-attachments/assets/55f9c2b2-9f59-41fe-bbdd-b4c742815d89" width="400px">

5. Create and Running a Migration Task
<img src="https://github.com/user-attachments/assets/c89959a2-96ee-447d-a44d-d72e48b5db98" width="400px">
<img src="https://github.com/user-attachments/assets/0c84d26f-6c40-4a88-964b-36b65562def4" width="400px">

6. Monitor and Check the Migration Task output by using MySQL Workbench

7. Create Lambda Function
   
8. Create DynamoDB Database and Table
<img src="https://github.com/user-attachments/assets/c8bc0a95-c277-4a81-8bf1-15dcea4543b9" width="400px">



