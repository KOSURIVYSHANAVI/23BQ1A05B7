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