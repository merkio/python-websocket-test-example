# python-websocket-test-example

Part 1:
 - For subscription first I need to check that I can subscribe and get a valid response.
 Then I should change the state of the subscription object and then check that I get the valid data from the server.
Subscription is not working if on any stage of this flow I get the wrong response or data.
 - If the user lifecycle is too long than I prefer to start with a splitting lifecycle to the smaller cases.
 A big test can be failed in the early stages and then you should restart the test after the fix to find another bug.
If you split a big test you can find more bugs in one launch.
 - I would launch tests or check new functionality on the dev server after that I would test this functionality 
 in a testing environment with other services and then if there is a release candidate environment or environment 
 with a few users I would check new features in this environment if there is something wrong.
  - Better to start testing inside clusters on a dev server before that code even merges to the master.
  For this purpose, I prefer to use a CI server. I think maybe a good solution to trigger the tests on dev server 
  when you create a PR or maybe launch tests manually. Also, I would run tests also in every stage of the development process 
  but with a different amount of tests, e.g. on dev you can run only specific tests, 
  in a testing environment better run all regression tests before a release.  
 - Language depends on the technologies on the project and preferences.
 
 Part 2:
- This project contains small example how you can test the websocket connection.
  This project is very simple and doesn't contain any additional functionality, e.g. logging and report tools.
  Also, to launch the tests you need to set environment variables. 
  I choose to check response schema first because is a faster way to check that basic functionality works.
  For more complex scenarios, I would add more functionality to change the state a ticket and instrument 
  to check that subscription works correct.
  - For REST API testing I have another example project here: https://github.com/merkio/rest-assured-example
