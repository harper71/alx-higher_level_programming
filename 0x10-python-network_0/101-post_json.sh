#!/bin/bash
# post a json file to url/ api
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
