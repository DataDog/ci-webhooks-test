#!/bin/sh

yarn global add @datadog/datadog-ci

datadog-ci trace --tags foo:bar --name "🚀" -- echo "Ship it"
