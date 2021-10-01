#!/bin/sh

git clone https://github.com/DataDog/datadog-ci.git

cd datadog-ci

git checkout edrevo/capture-error-message

yarn install

yarn prepack

./dist/index.js trace --tags foo:bar --name "🚀" ../customspanschildren.sh
