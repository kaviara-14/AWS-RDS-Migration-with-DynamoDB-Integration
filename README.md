# DMS-Migration

Migrating an on-premises MySQL database to Amazon RDS MySQL by using AWS Database Migration Services (DMS).After the migration is completed, we are invoking a Lambda function. That Lambda function checks and retrieves the newly added records from the RDS MySQL Database and inserts them into AWS DynamoDB Database.

# Project Steps
1. Create Local Mysql Database and table for the source Database

![Screenshot 2024-08-04 112731](https://github.com/user-attachments/assets/dc5e33f6-e7ad-48ac-9fa1-3be6cfe7e727)

2. Create RDS MySQL Database for the target Database

![Screenshot 2024-08-03 155124](https://github.com/user-attachments/assets/19d6e4df-8a93-4821-8f60-d09e5fceba91)


3. Create Replication Instance

![Screenshot 2024-08-03 155153](https://github.com/user-attachments/assets/700a9bce-7016-43ad-b06d-d8bfd7866a82)


4. Create Target and Source Endpoints

![Screenshot 2024-08-03 155212](https://github.com/user-attachments/assets/55f9c2b2-9f59-41fe-bbdd-b4c742815d89)

5. Create and Running a Migration Task

![Screenshot 2024-08-03 155321](https://github.com/user-attachments/assets/c89959a2-96ee-447d-a44d-d72e48b5db98)
![Screenshot 2024-08-03 155257](https://github.com/user-attachments/assets/0c84d26f-6c40-4a88-964b-36b65562def4)


6. Monitor and Check the Migration Task output by using MySQL Workbench

![Screenshot 2024-08-03 155047](https://github.com/user-attachments/assets/8c92de38-865f-49b7-8389-764a62c5d140)

7. Create Lambda Function
8. Create DynamoDB Database and Table

![Screenshot 2024-08-03 155426](https://github.com/user-attachments/assets/576d6144-5545-412b-91c1-bdb75890098c)


