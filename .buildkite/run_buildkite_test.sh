echo "Clearing test cache"
go clean -testcache

echo "Running Go tests"
gotestsum --format testname --junitfile test.xml

exit_code=$?

set -e
echo "Uploading XML to Data Dog"
datadog-ci junit upload --service carlos-test test.xml

ls -l test.xml | awk '{print $4}' | tr -d '\n' | buildkite-agent meta-data set "dd_metrics.junit.size"

echo "Exiting with ${exit_code}"
exit ${exit_code}
