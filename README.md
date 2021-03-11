***Create database and pip install package**********


********MongoDB*********


use itproger

createCollection("employees", {autoIndexId: true})

db.employees.insertOne({'name': 'Roger', 'surname': 'Federer', 'phone': '3702881212', 'email': 'federer@gmail.com', 'address': 'Basel, Switzerland'})

db.employees.createIndex({'phone':1, 'email':1}, {unique: true})


<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/home.png" alt="home"/>

<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/last.png" alt="last"/>

<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/add.png" alt="add"/>

<img src="https://github.com/Alpaca00/DataEmployees/blob/main/img/update.png" alt="update"/>


