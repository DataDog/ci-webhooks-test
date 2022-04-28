import os
import sys
import requests

def get_buildkite_env():
    return {k: v for k, v in os.environ.items() if k.startswith("BUILDKITE_") and ("KEY" not in k or "TOKEN" not in k or "SECRET" not in k)}


def send_metrics(level, ci_env, metrics, provider):
    paylaod = {
        "data": {
            "type": "ci_custom_metric",
            "attributes": {
                "provider": provider,
                "ci_level": level,
                "ci_env": ci_env,
                "metrics": metrics,
            },
        },
    }

    res = requests.post("https://dd.datad0g.com/api/v2/ci/pipeline/metrics", json=paylaod,
        headers={"DD-API-KEY": os.environ["DD_API_KEY"]})
    if res.status_code >= 300:
        try:
            print(f"Error: {res.json()}")
        except Exception:
            print(f"Error: {res.text}")
        res.raise_for_status()


def send_tags(level, ci_env, tags, provider):
    paylaod = {
        "data": {
            "type": "ci_custom_tag",
            "attributes": {
                "provider": provider,
                "ci_level": level,
                "ci_env": ci_env,
                "tags": tags,
            },
        },
    }

    res = requests.post("https://dd.datad0g.com/api/v2/ci/pipeline/tags", json=paylaod,
        headers={"DD-API-KEY": os.environ["DD_API_KEY"]})
    if res.status_code >= 300:
        print(f"Error: {res.json()}")
        res.raise_for_status()


def main():
    if len(sys.argv) < 4:
        sys.exit(1)

    level = sys.argv[2]
    if level == "pipeline":
        level = 0
    elif level == "job":
        level = 1
    else:
        sys.exit(1)

    print(f'{sys.argv[1]}: {sys.argv[3:]}')
    tags = {key_val[0]: key_val[1] for key_val in map(lambda x: x.split(":", 1), sys.argv[3:])}
    tags_or_metrics = sys.argv[1]
    if tags_or_metrics == "tags":
        send_tags(level, get_buildkite_env(), tags, "buildkite")
    elif tags_or_metrics == "metrics":
        send_metrics(level, get_buildkite_env(), tags, "buildkite")
    else:
        sys.exit(1)

main()
