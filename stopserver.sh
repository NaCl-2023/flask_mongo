#!/usr/bin/env bash
kill -9 $(netstat -nlp | grep :8081 | awk '{print $7}' | awk -F"/" '{ print $1 }')
