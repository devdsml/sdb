#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[3]:


import mysql.connector
mydb =mysql.connector.connect(host="localhost",
                             user="root",
                             password="",
                             database='test'
                              )
print(mydb)
mycursor =mydb.cursor(buffered=True)


# In[4]:


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[27]:


#rename db not posiible so create new db and rename old tables
mycursor.execute("CREATE DATABASE dtest1")
#mycursor.execute("RENAME TABLE test.employee TO dsmln.employee")


# In[ ]:


#delete any database
mycursor.execute("DROP DATABASE guvi")


# In[8]:


#zerofill fills values with zeroes before
mycursor.execute("CREATE TABLE ytable (x INT(8) ZEROFILL)")


# In[5]:


mycursor.execute("CREATE TABLE cemp(id INT unsigned NOT NULL AUTO_INCREMENT,name VARCHAR(150) NOT NULL,dept VARCHAR(150) NOT NULL,birth DATE NOT NULL,PRIMARY KEY (id))")


# In[9]:


mycursor.execute("CREATE TABLE lucky(salary INT(10),dept varchar(20),cmp varchar(20))")


# In[7]:


#describe table 
mycursor.execute("DESCRIBE cemp")
for x in mycursor:
  print(x)


# In[13]:


mycursor.execute("INSERT INTO cemp(name,dept,birth) VALUES ('dept1','name1','1900-03-02'),('dept2','name2','2001-02-02')")


# In[14]:


#change to another db
mycursor.execute("USE dtest1")


# In[16]:


mycursor.execute("SELECT * FROM dattimstmp WHERE dtstrng='April'")
#mycursor.execute("DELETE * FROM dattimstmp WHERE dtstrng='April'")
for x in mycursor:
  print(x)


# In[11]:


mycursor.execute("CREATE TABLE employee(cid INT(10),dept varchar(20),name varchar(20))")


# In[12]:


#insert values
mycursor.execute("INSERT INTO employee(cid,dept,name) VALUES ('1', 'd1', 'name1'), ('2', 'd2', 'name2')")


# In[13]:


#rename db not possible so create new db and rename old tables
#mycursor.execute("CREATE DATABASE dsmln")
mycursor.execute("RENAME TABLE test.lucky TO dsmln.lucky")


# In[14]:


#display tables
mycursor.execute("SHOW TABLES IN dsmln")
for x in mycursor:
    print(x)


# In[15]:


#add column at begginning
mycursor.execute("ALTER TABLE lucky ADD newcol VARCHAR(10) FIRST")


# In[17]:


#add coloumn after specific col
mycursor.execute("ALTER TABLE lucky ADD aftercol VARCHAR(10) AFTER newcol")


# In[18]:


#modify col name 
mycursor.execute("ALTER TABLE lucky CHANGE COLUMN aftercol modcol int")


# In[20]:


#delete a column
mycursor.execute("ALTER TABLE lucky DROP COLUMN cmp")


# In[24]:


mycursor.execute("SHOW TABLES IN dsmln WHERE TABLES_in_dsmln ='employee'")
for x in mycursor:
    print(x)


# In[26]:


#delete only values without deleting table structure
mycursor.execute("TRUNCATE employee")


# In[28]:


mycursor.execute("USE dtest1")


# In[29]:


mycursor.execute("CREATE TABLE dattimstmp (dtin DATE)")


# In[30]:


mycursor.execute("INSERT INTO dattimstmp (dtin) VALUES ( CURDATE())")
mycursor.execute("INSERT INTO dattimstmp (dtin) VALUES ( CURRENT_DATE())")
mycursor.execute("INSERT INTO dattimstmp (dtin) VALUES (CURTIME())")
mycursor.execute("INSERT INTO dattimstmp (dtin) VALUES (CURRENT_TIMESTAMP())")
mycursor.execute("INSERT INTO dattimstmp (dtin) VALUES (CURRENT_TIME())")
mycursor.execute("INSERT INTO dattimstmp (dtin) VALUES (NOW())")
mydb.commit()


# In[33]:


mycursor.execute("ALTER TABLE dattimstmp ADD dtstrng VARCHAR(255)")


# In[34]:


mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES ( CURDATE())")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES ( CURRENT_DATE())")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (CURTIME())")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (CURRENT_TIMESTAMP())")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (CURRENT_TIME())")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (NOW())")#date and time
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (MONTHNAME(NOW()))")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (DAYNAME(NOW()))")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (HOUR(NOW()))")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (MINUTE(NOW()))")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (DATE_ADD(NOW(),INTERVAL -10 DAY))")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (DATE_FORMAT(NOW(),'%W %D %M %Y %T %H'))")
mycursor.execute("INSERT INTO dattimstmp (dtstrng) VALUES (UTC_DATE())")#UTC_TIME,UTC_TIMESTAMP
mydb.commit()


# In[4]:


mycursor.execute("CREATE TABLE student(st_id INT AUTO_INCREMENT,name VARCHAR(20),major VARCHAR(20), PRIMARY KEY(st_id))")


# In[12]:


mycursor.execute("INSERT INTO student VALUES (4,'jane','biology'),(5,'radha','ece'),(6,'jaya','eee')")


# In[13]:


mycursor.execute("SELECT * FROM student")
for i in mycursor:
    print(i)


# In[14]:


mycursor.execute("UPDATE student SET name='sam' WHERE st_id=4")


# In[15]:


mycursor.execute("SELECT * FROM student")
for i in mycursor:
    print(i)


# In[16]:


mycursor.execute("ALTER TABLE student ADD newcol VARCHAR(10) FIRST")


# In[17]:


mycursor.execute("INSERT INTO student VALUES ('new1',14,'jane','biology'),('new2',15,'radha','ece'),('new3',16,'jaya','eee')")


# In[18]:


mycursor.execute("SELECT * FROM student")
for i in mycursor:
    print(i)


# In[20]:


mycursor.execute("DELETE FROM student WHERE newcol='new2'")


# In[21]:


mycursor.execute("SELECT * FROM student")
for i in mycursor:
    print(i)


# **ORDER BY ,IN **

# In[27]:


#mycursor.execute("SELECT student.name,student.major FROM student LIMIT 2")
mycursor.execute("SELECT name,major FROM student ORDER BY major,name DESC")
for i in mycursor:
    print(i)


# In[32]:


mycursor.execute("SELECT * FROM student WHERE major IN('ece','eee') and st_id<8")
for i in mycursor:
    print(i)


# In[34]:


mycursor.execute("SELECT COUNT(major) AS Totalm FROM student")
for i in mycursor:
    print(i)


# #GET INPUT FROM USER and INSERT

# In[41]:



a=input()
b=input()
c=input()
d=input()
query="INSERT INTO student VALUES (%s,%s,%s,%s)"
mycursor.execute(query,(a,b,c,d))


# In[42]:


mycursor.execute("SELECT * FROM student")
for i in mycursor:
    print(i)
    
#unique and check
#mycursor.execute("CREATE TABLE u (no INTEGER,name TEXT UNIQUE,school VARCHAR(20),age INT CHECK(age<18)) ")    


# In[36]:


mycursor.execute("CREATE TABLE employee ( emp_id INT PRIMARY KEY, first_name VARCHAR(40),  last_name VARCHAR(40),  birth_day DATE,  sex VARCHAR(1),   salary INT,   super_id INT,  branch_id INT )")


# In[38]:



'''CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);

CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);'''
'''
ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

CREATE TABLE works_with (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);

CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);'''


'''-- Corporate
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);

-- Scranton
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);

INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');

UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);'''

'''
-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);'''
get_ipython().system('pip install tabulate')


# In[40]:


from tabulate import tabulate

mycursor.execute("SELECT * FROM employee ORDER BY salary DESC")
out=mycursor.fetchall()
print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))


# In[45]:


mycursor.execute("SELECT first_name AS forename FROM employee")
out=mycursor.fetchall()
print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))


# In[46]:


mycursor.execute("SELECT DISTINCT sex FROM employee")
for i in mycursor:
    print(i)
                 


# **Aggregate FUNcTIONS - COUNT,SUM,AVG,MIN,MAX**

# In[48]:


mycursor.execute("SELECT COUNT(emp_id) FROM employee where birth_day>'1971-01-01'")
for i in mycursor:
    print(i)


# In[53]:


mycursor.execute("SELECT AVG(salary) FROM employee WHERE sex='F'")
for i in mycursor:
    print(i)


# In[54]:


mycursor.execute("SELECT SUM(salary) FROM employee")
for i in mycursor:
    print(i)


# **GruoupBY**

# In[56]:


#count of female,male
mycursor.execute("SELECT COUNT(sex),sex FROM employee GROUP BY sex")
for i in mycursor:
    print(i)


# In[57]:


#total sales of each salesman
mycursor.execute("SELECT SUM(total_sales),emp_id FROM works_with GROUP BY emp_id")
for i in mycursor:
    print(i)


# In[58]:


#total sales of each client
mycursor.execute("SELECT SUM(total_sales),client_id FROM works_with GROUP BY client_id")
for i in mycursor:
    print(i)


# **HAVING**

# In[7]:


mycursor.execute("SELECT client_id, SUM(total_sales) FROM works_with GROUP BY client_id HAVING SUM(total_sales) BETWEEN 20000 AND 30000 ORDER BY SUM(total_sales)")
for i in mycursor:
    print(i)


# **Operators**

# In[59]:


#find any client who are LLC
#  wildcsrd %means any char 
mycursor.execute("SELECT * FROM client WHERE client_name LIKE '%LLC'")
for i in mycursor:
    print(i)


# In[60]:


mycursor.execute("SELECT * FROM branch_supplier WHERE supplier_name LIKE '%ball%'")
for i in mycursor:
    print(i)


# In[63]:


#find employee with birthdate is october 
#matches four char and -10
#underscore - matches one char 
mycursor.execute("SELECT * FROM employee WHERE birth_day LIKE '____-10%'")
for i in mycursor:
    print(i)


# **UNION**

# In[64]:


#combine two select statements
#should have same no of columns ,datatypes

mycursor.execute("SELECT first_name FROM employee UNION SELECT branch_name FROM branch")
for i in mycursor:
    print(i)


# **JOINS**

# In[69]:


#find all branches and names of managers
#mycursor.execute("INSERT INTO branch VALUES(4,'Buffalo',NULL,NULL)")
#inner join 
mycursor.execute("SELECT employee.emp_id,employee.first_name,branch.branch_name FROM employee JOIN branch ON employee.emp_id=branch.mgr_id")
for i in mycursor:
    print(i)


# In[71]:


#left join 
mycursor.execute("SELECT employee.emp_id,employee.first_name,branch.branch_name FROM employee LEFT JOIN branch ON employee.emp_id=branch.mgr_id")
for i in mycursor:
    print(i)


# In[72]:


#right join 
mycursor.execute("SELECT employee.emp_id,employee.first_name,branch.branch_name FROM employee RIGHT JOIN branch ON employee.emp_id=branch.mgr_id")
for i in mycursor:
    print(i)


# **NESTED QUERIES**

# In[75]:


mycursor.execute("SELECT employee.first_name,employee.last_name FROM employee WHERE employee.emp_id IN(SELECT works_with.emp_id FROM works_with WHERE works_with.total_sales > 30000)")
for i in mycursor:
    print(i)


# **TRIGGERS**

# DELIMITER $$
# CREATE
#     TRIGGER my_trig BEFORE INSERT
#     ON  employee
#     FOR EACH ROW BEGIN
#       ISERT INTO trig_testable values('added new emp');
#     END$$
# DELIMITER ;    

# In[ ]:




