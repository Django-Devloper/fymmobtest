Description :

Djnago rest api web appto calculate fare.

USER INTERFACE AND API.
Each user need to login with userid and password to authonticate 
for test :
  Userid = Deepak 
  Password = Dipak@123
  ![image](https://user-images.githubusercontent.com/107532268/198753389-27bdc68c-9a74-4bc1-bd04-f4e8ea8131d2.png)

![image](https://user-images.githubusercontent.com/107532268/198753413-ce4d2a4e-4c5f-445b-94b8-f749b5ab1ddc.png)

after login it will redirect to passanger information with each trip details .

![image](https://user-images.githubusercontent.com/107532268/198646287-25b0c0f0-e64a-458d-9168-f05a8a07b684.png)



ADMIN USER INTERFACE
Userid - Modi
Passwod -Dipak@123

![image](https://user-images.githubusercontent.com/107532268/198296482-917f10cf-8f6d-4247-b5a9-87ce62fb18eb.png)

there is two magor data table to work 
1. Price option - it help to enter multiple price option and active one of them for auto calculation :

![image](https://user-images.githubusercontent.com/107532268/198296987-50ff568a-9b42-4c86-8115-041fed6dd696.png)

Make sure isactive status should be False before adding new price option with new Active status true . (only one price option should be True )
![image](https://user-images.githubusercontent.com/107532268/198297779-4cc7c70c-b300-4044-a7e4-ff31cb725780.png)

2. Trips Details - contain every user trips infornmation to add new details click on add trip button .

![image](https://user-images.githubusercontent.com/107532268/198753485-02b7f734-fcba-4f6c-9c12-8843c01d468a.png)

![image](https://user-images.githubusercontent.com/107532268/198298441-82881d71-a4f7-439c-954a-22a683b0d4ab.png)

fare details is read only fields automatic select price option isactive true price option 

to run this app 
pip install -r requirements.txt
rum python.exe manage.py runserver  
it will direct you to login page  plese login as user or admin credetial mentioned above .
