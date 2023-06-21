# Architecture for 'Animal Tinder'
1. MySQL database for storing user data and interactions
2. Backend REST API (GET, POST requests) server for serving website and apis

## Database (MySQL) tables

### User (user)
```
{
    id: a unique identifier for the user,
    email: the user's email,
    password: the user's password
}
```

SQL:
```
CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
```

### User Profile (user_profile)
```
{
    id: the id of the profile,
    user_id: this profile belongs do the user with the id matching this one,
    display_name: the display name of the user,
    bio: a short description for the user,
    pfp_url: an image url 
}
```
SQL:
```
CREATE TABLE user_profile (
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  display_name VARCHAR(255) NOT NULL,
  bio VARCHAR(255),
  pfp_url VARCHAR(255),
  PRIMARY KEY (id)
);
```
