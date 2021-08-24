#!/bin/sh

git clone https://github.com/DataDog/datadog-ci.git

cd datadog-ci

git checkout 9ee549e0f26b932cf152ef2c2ff31cf38326f36f

yarn install

yarn launch trace ../customspanschildren.sh