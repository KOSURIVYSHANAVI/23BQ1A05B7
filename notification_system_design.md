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

STAGE3:validating the given query
given :

select * from notifications
where studentId=1042 AND is_read=false
ORDER_BY createdAt DESC;

yes,logically the above Query is correct,the query fetches the notifications that are unread in order of latest first

It is slow because no any particular indexing the queries searches all the data in the given database and stores the unread data and then it displays in sorted order high time complexity around of 0(n log n),so it is slow

solution i think:
create INDEX i on notifications(studentID, isRead, createdAt DESC);
Filters studentID,isRead,sorts by createdAt so need of sorting,only a complextiy of 0(n) saves some time

Indexing:
Indexing gives output correct,but not a good idea it increases the cost for storing them and Insertions,deletions,updations can be slower compared to before,it is not a good idea i will explain the conseques to my team mate who proposed this idea.
Another possible Query:

select id, message, createdAt
from notifications
WHERE studentID = 1042
AND isRead = false
ORDER BY createdAt DESC;

better compared to first

Query to get students who got the placement notification last week i.e last 7 days:

select DISTINCT studentID from notifications where notificationType = 'placement' AND createdAt >= NOW() - INTERVAL 7 DAY;

we use distinct to avoid getting same student more than one and to specify condition we used where type must be placement and createdAt >= NOW() - INTERVAL 7 DAY, is used to get the details from now within a span of 1 week, we not mention it we will get all students who got placement notifications.