# Login and Register Pages using Flask and Mysql
This is a basic Flask and Mysql application. The main idea in this project is to connect Flask and Mysql and use them together. Here there are two pages. One page is main home page and the other page is user_login_page. Main page contains login and register processes, user_login_page contains a message that user's email and user's visit time. Below picture shows the home page.(localhost:5000/)

![home_page](https://user-images.githubusercontent.com/42489236/172342728-966390b4-02b3-415b-a5dd-651e07bbb182.png)

Below picture shows the user_login_page.

![user login page](https://user-images.githubusercontent.com/42489236/172343221-5c092225-192c-41cc-8c4d-728bb8219a09.png)

#### Usage:

Be at the same directory with the project files. In terminal run 'python app.py'. After running go to localhost:5000 and use the page. credentials.json contains mysql username, password and database name. Change credentials file yourself. functions.py file contains some functions and main app.py file calls some functions from that file. And the last file templates contain only one login.html file. login.html file contains the html information about the home page.
