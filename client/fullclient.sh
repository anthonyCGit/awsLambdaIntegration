#!/bin/bash
# JSON object to pass to Lambda Function
# Replace .txt file with one of the sample files.
story=$( cat -s houn-med.txt | sed '$ ! s/$/\\n/' | tr -d '\n' | tr -d '\"' | tr -d "\'" )
json="{\"story\":\"$story\"}"
echo "JSON INPUT:"
echo $json | jq
echo ""
echo "Invoking Extract Lambda function using API Gateway"
time output=`curl -s -H "Content-Type: application/json" -X POST -d "$json" https://REPLACE-WITH-API-LINK.amazonaws.com/storyExtract_dev`
echo ""
echo ""
echo "JSON RESULT:"
echo $output | jq
echo ""
echo ""
words=$( echo $output | jq '.message' )
json="{\"words\":$words}"
echo "JSON INPUT:"
echo $json | jq
echo ""
echo "Invoking Transform/Load Lambda function using API Gateway"
time output=`curl -s -H "Content-Type: application/json" -X POST -d "$json" https://REPLACE-WITH-API-LINK.amazonaws.com/storyTransform_dev`
echo ""
echo ""
echo "JSON RESULT:"
echo $output | jq
