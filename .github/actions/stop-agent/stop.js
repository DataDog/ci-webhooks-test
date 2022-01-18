const { spawnSync } = require('child_process');
const core = require('@actions/core');

core.info('Stopping datadog agent in docker container');
const child = spawnSync(`docker exec -t ${core.getInput('containerName', { required: true })} agent stop`, { timeout: 300000 });
if (child.status === 0) {
    core.info('Datadog agent stopped');
} else {
    core.error('Datadog agent could not be stopped');
}
