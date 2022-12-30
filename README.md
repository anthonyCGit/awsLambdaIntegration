# awsLambdaIntegration
**Goal:** Build a program that links multiple serverless functions to perform an operation on given input.

**Outcome:** Used AWS Lambda to link 2 lambda functions to take in a story sample and produce a new story.

**Team:** Leader and Programmer in team of 4

**Languages:** Python, Bash

**Notes:** I worked on the handler functions for each Lambda as well as part of the Bash script.

**Instructions:**
1) Create 2 AWS Lambda Functions: one for the extractStory.zip and one for the transformStory.zip
2) For each Lambda function, create a corresponding REST API Gateway to call the function.
3) Replace the first link in the Bash script with the extractStory API link and the second with the transformStory API link.
4) In the Bash script, change the .txt to one of the provided sample text files.
5) Run the Bash script from the command line.
