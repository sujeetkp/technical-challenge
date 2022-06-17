#!/bin/bash

echo "Enter your object: "
read object
echo "Enter your key: "
read key

get_value(){

  object=$1
  key=$2

  temp=$(echo $key | sed 's/\//\./g') 
  value=$(echo $object | jq ".$temp")
  
  if [[ "$value" != "null" ]]; then 
    echo $value
  else
    echo "Not Found"
  fi

}

#object='{"a":{"b":{"c":"d"}}}'
#key='a/b/c'

get_value $object $key

