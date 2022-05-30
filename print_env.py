import re
import os
import json


envs = {}
for k, v in os.environ.items():
    if k.startswith("GITHUB_") and not re.search('(PASS)|(TOKEN)|(SECRET)|(KEY)', k) and v:
        envs[k] = v

print(f'ci.env_vars:{json.dumps(envs, sort_keys=True, separators=(',', ':'))}')
