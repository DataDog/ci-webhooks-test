#!/bin/sh

git clone https://github.com/DataDog/datadog-ci.git

git checkout edrevo/capture-error-message

cd datadog-ci

yarn install

yarn prepack

./dist/index.js trace --tags foo:bar --name "🚀" ../customspanschildren.sh
