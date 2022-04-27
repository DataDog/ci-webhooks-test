echo "Adding tags"
python3 .buildkite/custom_tags.py job "go.version:`go version`" "gotestsum.version:`gotestsum --version`"

echo "Clearing test cache"
go clean -testcache

echo "Running Go tests"
gotestsum --format testname --junitfile test.xml

exit_code=$?

set -e
echo "Uploading XML to Data Dog"
datadog-ci junit upload --service carlos-test test.xml

echo "Exiting with ${exit_code}"
exit ${exit_code}
