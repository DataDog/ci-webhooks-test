import re
import os


envs = []
for k, v in os.environ.items():
    if k.startswith("GITHUB_") and not re.search('(PASS)|(TOKEN)|(SECRET)|(KEY)', k) and v:
        envs.append(f'{k}={v}')

print(f'ci.env_vars:{",".join(envs)}')
