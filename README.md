# APImachinelearning
Machine Learning (ML) is a valuable tool for jobs that can't be explicitly coded, such image classification. Deployment is a critical step in the machine learning process. The approach for the REST API that we aim to provide is image categorization. We'll utilize Google Image to look for food images because we're using food as our data set, thus we'll do a food photo query. Following that, the server will provide the response, which will be a collection of food photos.

# Kafka Implementation
Kafka is a distributed streaming platform that makes data integration between systems easier. A stream is a data pipeline that your apps use to receive data on a regular basis.

The Kafka system is made up of three basic parts:

A Producer is a service that generates data that has to be broadcast, which I implemented with the Flask API.

A Broker: This is Kafka himself, who serves as a go-between for the producer and the consumer. It makes use of APIs to obtain and broadcast data.

A consumer is a service that makes use of the information that the broker will disseminate.

Creating a basic streaming application that displays a video file from our producer in a web browser.

# REST API Implementation
Flask Restful is a Flask plugin that allows you to create REST APIs in Python with Flask as the backend. It promotes best practices and is simple to implement. If you're already familiar with flask, restful is a breeze to learn.

The main building block in flask restful is a resource. Each resource can be connected with several methods, such as GET, POST, PUT, DELETE, and so on. For example, there may be a resource that, everytime a get request is submitted to it, calculates the square of an integer. Each resource is a class that derives from flask restful's Resource class. We can add our own resource to the api and specify a URL route for the associated resource once the resource has been established and configured.
