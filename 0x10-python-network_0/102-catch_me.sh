#!/bin/bash
# catch an error an prints "You got me!"
curl -s --location --request PUT "http://0.0.0.0:5000/catch_me" --data ""
