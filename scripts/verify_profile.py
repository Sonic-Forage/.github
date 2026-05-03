#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
readme=root/'profile/README.md'
text=readme.read_text()
required=[
 'Sonic Forage','mycelium','ecosystem','sonicforge-starter-kit','rave-culture-field-guide',
 'rave-autonomous-launch-game-plan','rave-harm-reduction-community-kit','rave-harm-reduction-demo-fork',
 'sonic-forage-asset-vault','sonic-forage-autonomous-booking-kit','sonic-forage-trip-manual',
 'sonic-forage-master-prompt-arcade','Strawberry AGI Snake','MASTER_PROMPT','COMFYUI_BASE_URL',
 'VOICE_PROVIDER','closed_until_human_yes','prompts','payloads','tags','Unicode'
]
missing=[s for s in required if s not in text]
if missing:
    raise SystemExit('missing required profile terms: '+', '.join(missing))
# Ensure real private endpoint patterns are not in the profile.
for pattern in [r'https?://[^\s)]+(?:modal\.run|ngrok|trycloudflare)[^\s)]*', r'ghp_[A-Za-z0-9_]+', r'sk-[A-Za-z0-9_]+']:
    if re.search(pattern, text, flags=re.I):
        raise SystemExit('unsafe pattern found: '+pattern)
# Basic markdown link sanity for local raw banner and public URLs.
links=re.findall(r'\[[^\]]+\]\((https://[^)]+)\)', text)
if len(links) < 8:
    raise SystemExit('expected at least 8 public links')
print('SONIC FORAGE PROFILE VERIFY OK')
print('profile bytes:', readme.stat().st_size)
print('public links:', len(links))
print('required terms:', len(required))
