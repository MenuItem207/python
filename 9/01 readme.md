# Login and Sign up API

## What is an API?
- an API (application programming interface) is a way for 2 or more computer programs to communicate / interface
- REST is an API structure that includes GET and POST
- Used for logins, fetching data, load images, updating profiles, website etc

## MYSQL
- its a database, think excel or spreadsheets, mysql is a programming database built for speed
- its structure is simple: databases, tables, rows and columns

### Databases (MYSQL)
- MYSQL databases are like separate excel files, each database has its own tables

### Tables (MYSQL)
- MYSQL tables are like pages in excel files, each table has a different use   
- For example a commonly found table in mysql includes 'User' to store details like email and password on the user
- Another one could be 'Post' where different posts posted by the user are stored

### Rows and Columns (MYSQL)
- each 'table' in mysql has rows and columns
- A row is just a new entry in the table, similar to excel
- A column has a name and a type, for example in the table user that has email and password, email is a column with the name 'email' of type 'TEXT'

### Running MYSQL
- MYSQL runs on a server, we'll download 'XAMPP' to allow a MYSQL server to run on your computer
- In real world applications, most servers are run in the cloud and accessed through the internet
- Go here and download XAMPP: https://www.apachefriends.org/download.html
- Once installed, run 'apache' and 'mysql', this is required everytime
- Click on 'admin' to manage your server