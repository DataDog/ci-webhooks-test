#!/bin/sh

git clone https://github.com/DataDog/datadog-ci.git

cd datadog-ci

git checkout 397c4b510cae3a9b57b686cb7fcc95513f530c1d

yarn install

yarn launch trace ../customspanschildren.sh