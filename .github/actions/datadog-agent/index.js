const core = require('@actions/core');
const { spawnSync } = require('child_process');

core.info('Starting docker Datadog agent')

const dockerPull = spawnSync('docker', [
    'pull',
    core.getInput('registryPath', { required: true }),
    ],{ stdio: 'inherit' });
if (dockerPull.error || dockerPull.status !== 0) {
    core.setFailed('could not pull docker image');
    process.exit(1)
}

core.info('Running agent');
const dockerRun = spawnSync('docker', [
    'run',
    '-d',
    '--name', core.getInput('containerName', { required: true }),
    '-v', '"/var/run/docker.sock":"/var/run/docker.sock":ro',
    '-v', '"proc/":/"host/proc/":ro',
    '-v', '"/sys/fs/cgroup/":"/host/sys/fs/cgroup":ro',
    '-e',  `DD_API_KEY=${core.getInput('apiKey', { required: true })}`,
    '-e', 'DD_INSIDE_CI=true',
    '-e', 'DD_HOSTNAME=none',
    '-e', `DD_SITE=${core.getInput('site', { required: true })}`,
    core.getInput('registryPath', { required: true }),
    ], { stdio: 'inherit' });

if (dockerRun.error || dockerRun.status !== 0) {
    core.setFailed('could not run docker image');
    process.exit(1)
}

core.info('Started docker agent');