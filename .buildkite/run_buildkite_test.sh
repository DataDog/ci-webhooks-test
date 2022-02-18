#!/bin/bash

echo "Clearing test cache"
go clean -testcache

echo "Running Go tests"
gotestsum --format testname --junitfile test.xml

exit_code=$?

set -e
echo "Uploading XML to Data Dog"
datadog-ci junit upload --service carlos-test test.xml

set -x
echo "$(ls -l test.xml | awk '{print $5}' | tr -d '\n')"
size=$(ls -l test.xml | awk '{print $5}' | tr -d '\n')

buildkite-agent meta-data set "dd_metrics.buildkite.junit_size_bytes" $size

echo "Exiting with ${exit_code}"
exit ${exit_code}
