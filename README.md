# icav_project

please run requirements.txt before run the project .

In this Project one Docker Image is present.

There are Two end points of this project to see the books.csv data

1. http://127.0.0.1:5000/books/v1/get-book-data/?rows=3 , This end point is the GET Request using the parameter rows. you can just put the number of rows and it will give only those rows data.

2. http://127.0.0.1:5000/books/v1/get-book-filter-data/ , This end point is the POST Request using the json parameter below, you can filter the books.csv data using the keys which is present in books.csv file as column. json eg:- {"authors":"Bayo Ogunjimi, Abdul Rasheed Na'allah"}

3. One Test file is also included in this project in which some test cases are present.

NOTE :- If the data is not coming in postman pretty format please check the raw format as well.
