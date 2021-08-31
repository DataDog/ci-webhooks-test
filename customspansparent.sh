#!/bin/sh

git clone https://github.com/DataDog/datadog-ci.git

cd datadog-ci

git checkout edrevo/custom-spans

yarn install

yarn prepack

./dist/index.js trace ../customspanschildren.sh
