#!/bin/bash
# checks for  all OPTIONS command on https
curl -sI "$1"| grep "Allow" | cut -d " " -f 2-
