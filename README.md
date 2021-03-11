***Create database and pip install package**********


********MongoDB*********


use itproger

createCollection("employees", {autoIndexId: true})

db.employees.insertOne({'name': 'Roger', 'surname': 'Federer', 'phone': '3702881212', 'email': 'federer@gmail.com', 'address': 'Basel, Switzerland'})

db.employees.createIndex({'phone':1, 'email':1}, {unique: true})


<img src="" alt=""/>

<img src="" alt=""/>

<img src="" alt=""/>

<img src="" alt=""/>

<img src="" alt=""/>

<img src="" alt=""/>
