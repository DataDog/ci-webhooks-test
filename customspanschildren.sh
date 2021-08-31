#!/bin/sh

yarn launch trace --name "Say Hello" -- echo "Hello World"

yarn launch trace sleep 5

yarn launch trace --name "Fail" -- gfdjkghdfjk
