#!/bin/bash

# Changer l'échelle des applications à 5
docker-compose up --scale app1=5 --scale app2=5 --scale app3=5 -d