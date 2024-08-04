# DMS-Migration

Migrating an on-premises MySQL database to Amazon RDS MySQL by using AWS Database Migration Services (DMS).After the migration is completed, we are invoking a Lambda function. That Lambda function checks and retrieves the newly added records from the RDS MySQL Database and inserts them into AWS DynamoDB Database.

# Project Steps
1. Create an Local Mysql Database and table for the source Database
2. Create an RDS MySQL Database for the target Database
3. Create a Replication Instance
4. Create Target and Source Endpoints
5. Create and Running a Migration Task
6. Monitor and Check the Migration Task output by using MySQL Workbench
7. Create a Lambda Function
8. Create a DynamoDB Database and Table
