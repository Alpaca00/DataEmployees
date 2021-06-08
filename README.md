$ pip install -r requirements.txt


----MongoDB----
https://docs.mongodb.com/manual/installation/

--Сreate a database of names "itproger".-- 
> use itproger

--Before launch application you must to create collection for correct work.--

> createCollection("employees", {autoIndexId: true})

--Insert one person into the collection.--
> db.employees.insertOne({'name': 'John', 'surname': 'Doe', 'phone': '+1234567890', 'email': 'johndoe@gmail.com', 'address': 'undefined, undefined'})

--Create the index to display and search any person correctly.--
> db.employees.createIndex({'phone':1, 'email':1}, {unique: true})


<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/home.png" alt="home"/>

<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/last.png" alt="last"/>

<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/add.png" alt="add"/>

<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/update.png" alt="update"/>


