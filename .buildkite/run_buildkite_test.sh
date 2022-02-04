echo "Clearing test cache"
go clean -testcache

echo "Running Go tests"
gotestsum --format testname --junitfile test.xml

exit_code=$?

set -e
echo "Uploading XML to Data Dog"
DATADOG_API_KEY=datadog-ci junit upload --service carlos-test test.xml

echo "Exiting with ${exit_code}"
exit ${exit_code}
