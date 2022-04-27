import os
import sys
import requests

def get_buildkite_env():
    return {k: v for k, v in os.environ if k.startswith("BUILDKITE_") and ("KEY" not in k or "TOKEN" not in k or "SECRET" not in k)}

def send_tags(level, ci_env, tags, provider):
    paylaod = {
        "data": {
            "type": "ci_custom_tag",
            "attributes": {
                "provider": provider,
                "level": level,
                "ci_env": ci_env,
                "tags": tags,
            },
        },
    }

    requests.post("https://dd.datad0g.com/api/v2/ci/pipeline/tags", json=paylaod,
        headers={"DD-API-KEY": os.environ["DD_API_KEY"], "DD-APPLICATION-KEY": os.environ["DD_APP_KEY"]})


def main():
    if len(sys.argv) < 3:
        sys.exit(1)

    level = sys.argv[1]
    if level == "pipeline":
        level = 0
    elif level == "job":
        level = 1
    else:
        sys.exit(1)

    tags = {key_val[0]: key_val[1] for key_val in map(lambda x: x.split(":", 1), sys.argv[2:])}
    send_tags(level, get_buildkite_env(), tags, "buildkite")

main()
