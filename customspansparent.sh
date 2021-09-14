#!/bin/sh

git clone https://github.com/DataDog/datadog-ci.git

cd datadog-ci

yarn install

yarn prepack

./dist/index.js trace ../customspanschildren.sh
