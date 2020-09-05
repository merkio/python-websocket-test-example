# python-websocket-test-example

## Part 1:
 - For subscription first I need to check that I can subscribe and get a valid response.
 Then I should change the state of the subscription object and then check that I get the valid data from the server.
Subscription is not working if on any stage of this flow I get the wrong response or data.
 
 ## Part 2:
- This project contains small example how you can test the websocket connection.
  This project is very simple and doesn't contain any additional functionality, e.g. logging and report tools.
  Also, to launch the tests you need to set environment variables. 
  I choose to check response schema first because is a faster way to check that basic functionality works.
  For more complex scenarios, I would add more functionality to change the state a ticket and instrument 
  to check that subscription works correct.
  - For REST API testing I have another example project here: https://github.com/merkio/rest-assured-example
