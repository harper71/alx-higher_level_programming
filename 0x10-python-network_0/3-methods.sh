#!/bin/bash
# uses the DELETE command
curl -sI "$1"| grep "Allow" | cut -d " " -f 2-
