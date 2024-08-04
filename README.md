# DMS-Migration

Migrating an on-premises MySQL database to Amazon RDS MySQL by using AWS Database Migration Services (DMS).After the migration is completed, we are invoking a Lambda function. That Lambda function checks and retrieves the newly added records from the RDS MySQL Database and inserts them into AWS DynamoDB Database.

# Project Steps
1. Create Local Mysql Database and table for the source Database

![Screenshot 2024-08-04 112731](https://github.com/user-attachments/assets/d87cdd07-b18c-427a-aadb-3fce7372b0d0)

2. Create RDS MySQL Database for the target Database

![Screenshot 2024-08-03 155124](https://github.com/user-attachments/assets/d1312be1-1c64-49ec-84d2-e3ce799dfa40)

3. Create Replication Instance

![Screenshot 2024-08-03 155153](https://github.com/user-attachments/assets/ef94d601-686b-480f-93a3-0597015f7889)

4. Create Target and Source Endpoints

![Screenshot 2024-08-03 155212](https://github.com/user-attachments/assets/55f9c2b2-9f59-41fe-bbdd-b4c742815d89)

5. Create and Running a Migration Task

![Screenshot 2024-08-03 155321](https://github.com/user-attachments/assets/f8783fc9-0dfe-4d76-91ab-1b4e5359c8a7)
![Screenshot 2024-08-03 155330](https://github.com/user-attachments/assets/9fabf6cd-90b4-4dab-87df-7e537cf7b4c7)

6. Monitor and Check the Migration Task output by using MySQL Workbench

![Screenshot 2024-08-03 155047](https://github.com/user-attachments/assets/8c92de38-865f-49b7-8389-764a62c5d140)

7. Create Lambda Function
8. Create DynamoDB Database and Table

![Screenshot 2024-08-04 092355](https://github.com/user-attachments/assets/5b2a8af7-fb55-40bd-bc21-f16a06071e04)

