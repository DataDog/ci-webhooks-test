#!/bin/bash

set +e

attempts=0
datadog-agent health
exit_code=$?

until [[ $attempts -ge 50 ||  $exit_code -eq 0 ]]; do
    attempts=$((attempts+1))
    sleep_time=$(( attempts*10 < 60 ? attempts*10 : 60 ))
    echo "Waiting for agent to start up sleeping for ${sleep_time} seconds"
    sleep $sleep_time

    datadog-agent health
    exit_code=$?
done

if [[ $exit_code -ne 0 ]]; then
    echo "Could not start the agent"
    exit 1
fi
