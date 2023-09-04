# Project: STEDI-Human-Balance-Analytics

## Contents

+ [Problem Statement](#Problem-Statement)
+ [Project Discription](#Project-Discription)
+ [Project Datasets](#Project-Datasets)
+ [Project Files](#Project-Files)
+ [How To Run](#How-To-Run)

---
## Problem Statement

The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:
- trains the user to do a STEDI balance exercise
- has sensors on the device that collect data to train a machine-learning algorithm to detect steps
- has a companion mobile app that collects customer data and interacts with the device sensors

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

---

### Project Discription

In this project I extracted data produced by the STEDI Step Trainer sensors and the mobile app, and curated them into a data lakehouse solution on AWS. The intent is for Data Scientists to use the solution to train machine learning models. 

The Data lake solution is developed using AWS Glue, AWS S3, Python, and Spark for sensor data that trains machine learning algorithms.

AWS infrastructure is used to create storage zones (landing, trusted and curated), data catalog, data transformations between zones and queries in semi-structured data.

---

## Project Datasets

* Customer Records: from fulfillment and the STEDI website.  
* Step Trainer Records: data from the motion sensor.
* Accelerometer Records: data from the mobile app.

---

### Project Files 
This project consists of the following files:
+ `sql_queries.py` - This file contains Postgres SQL queries in string formate. 
+ `create_tables.py` - This script uses the sql_queries.py file to create new tables or drop old tables in the database.
+ `etl.py` - This script is used to build ETL processes which will read every file contained S3 bucket, copy its data into tables in the Redshift Cluster, then insert its values into the Star Schema using variables in sql_queries.py file.
+ `dwh.cfg` - This File contains the IAM role ARN, the path to S3 Datasets and the Redshift Cluster configurations.
+ `test.ipynb` - This notebook is used for testing purposes after finishing, to run queries on (you can also run queries in AWS Redshift query editor). 

---

### How To Run

Firstly, you need to create IAM Role that has read access to S3 bucket, then you need to create the Redshift Cluster and assosiate the IAM role to it. After that, you need to fill in the IAM role ARN and the Redshift Cluster configurations into the `dwh.cfg` file. Finally run `create_tables.py` file to drop and create the tables and then run `etl.py` to insert the data into the tables.
