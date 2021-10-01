#!/bin/sh

./dist/index.js trace --name "Say Hello" -- echo "Hello World"

./dist/index.js trace sleep 5

./dist/index.js trace --name "Fail" -- gfdjkghdfjk

./dist/index.js trace --name "Fail afain" -- ls -3
