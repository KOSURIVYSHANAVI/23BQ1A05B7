STAGE 1:
API End points that all required for handling real time notifiactions and with their possible json formats

1.GET notification from user:get is used to retreive data to use i.e to fetch
end point: GET/users/{id}/notifications
based of id of user the notifications can be send which is unique for everyone
for get no request body
expected response body:
[
  {
    "id": 1,
    "message": "Login successful"
  }
]

2.POST is used to add here they are sending notifications
end point :POST/notifications
Request body:
{
  "userId": 1,
  "message": "NEW Notifiaction"
}

Response body:
{
  "message": "Notification send sucussesfully",
  "notificationId": 1
}

3.DELETE is used to delete the particular notification by their unique id
end pont:DELETE/{id}/notifications
No any request body
Response body:
{
  "message": "Notification deleted successfully"
}

another one i.e 4.To know whether notification is readed or not
end point:PUT/notification/{id}/read
Request Body:
no any request body
Response Body:
{
    "message":"Notification is readed"
}


stage 2: Database for task in stage 1
2 tables needed to create one for notifications another one for the users data storage 
table 1:notifications which stores id along with user id,message which is in text format,and boolean value to check whwther it is readed or not.
notifications (
    id INT PRIMARY KEY,
    user_id INT,
    message TEXT,
    is_read BOOLEAN
)

table 2:users we are creating it to store users unique id and name we can also store other details like email...
users (
    id INT PRIMARY KEY,
    name VARCHAR
)
by these 2 tables an user can get any number of notifications

Problem:LARGE DATA VOLUME
by indexing of the user id we can actually solve the large amount of data rather than spreading same user all over the data,the data stored in less volume
It also causes overload this can be reduced by pagination,through which we can restrict only a particular no.of notifiactions can be seen on the screen

Queries:
SQL:
for insertion:
INSERT INTO notifications (user_id, message, status)VALUES (1, 'Login Success', 'unread');

for get:
select * from notifications;

get with some condtions like example retreive unread messages:
select * from notifications where status="unread";

REST APIS in stage1:
GET    /notifications?userId=1
POST   /notifications
PUT    /notifications/{id}