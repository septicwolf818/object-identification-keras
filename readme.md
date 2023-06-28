# Object Identification using AI model as a Django app

## About

This project uses Keras **ResNet50V2** model to predict object classes from the uploaded image.

## How to run

### 1. Clone repository

`git clone <repo_url>`

### 2. Enter into the repository directory

`cd <name_of_the_directory_where_repo_was_cloned>`

### 3. Install all requirements needed from `requirements.txt` file.

`pip3 install -r requirements.txt`

### 4. `cd` into `objectidentification` directory

`cd objectidentification`

### 5. Run Django server

`python3 manage.py runserver`

### 6. Open page in the web browser

[http://localhost:8000](http://localhost:8000)


## How to use

### 1. From Home Page navigate to Upload Image Page

### 2. Upload image using the form

### 3. After submiting you will see three results with:

- class name
- prediction score as percentage