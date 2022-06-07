import mysql.connector

def get_add_visit_time(email_val, pass_val, username, password, db_name):
    """
    Docstring:
    To verify the username and password for login. After that if the username and password is correct then increments the visit time one more.

    Parameters
    ----------
    email_val : Email address of the user.
    pass_val : Password of the user.
    username : Username to login the database. 
    password : Password to login the database.
    db_name : Name of the database.

    Returns
    -------
    bool and int value
        If returns true and a visit time value then direct to the admin page and write the visit time.
        If returns false and 0 then the username or password is incorrect.
    
    """
    mydb = mysql.connector.connect(host="localhost",user=username,password=password,database=db_name)
    my_cursor = mydb.cursor()

    sql_command = "SELECT * FROM members WHERE email=%s AND password=%s"
    val = (email_val, pass_val)

    my_cursor.execute(sql_command, val)

    if my_cursor.fetchall():
        mydb = mysql.connector.connect(host="localhost",user="yunus",password="123",database="mysql_db")
        my_cursor = mydb.cursor()
        
        my_cursor.execute("SELECT visit_time FROM members \
        WHERE email=%s AND password=%s", (email_val, pass_val))
        
        visit_val = my_cursor.fetchall()[0][0]
        
        my_cursor.execute("UPDATE members SET visit_time=%s \
        WHERE email=%s AND password=%s", (visit_val+1, email_val, pass_val))
        mydb.commit()
        
        return True, visit_val+1
    else:
        return False, 0

def register(email_val, pass_val, username, password, db_name):
    """
    Docstring:
    To register a user.

    Parameters
    ----------
    email_val : Email address of the user who wants to register.
    pass_val : Password of the user who wants to register.
    username : Username to login the database. 
    password : Password to login the database.
    db_name : Name of the database.

    Returns
    -------
    bool
        If returns true, it means the user register process is finished.
        If returns false, it means the user is already exists.
    
    """
    mydb = mysql.connector.connect(host="localhost",user=username,password=password,database=db_name)
    my_cursor = mydb.cursor()

    sql_command = "SELECT * FROM members WHERE email=%s"
    val = [email_val]

    my_cursor.execute(sql_command, val)

    if my_cursor.fetchall():
        return False
    else:
        sql_command = "INSERT INTO members(email, password, visit_time) VALUES (%s, %s, %s)"
        val = (email_val, pass_val, 1)
        
        my_cursor.execute(sql_command, val)
        mydb.commit()
        return True