#!/bin/bash
# uses the DELETE command
curl -sI | grep "Allow" | cut -d " " -f 2-
