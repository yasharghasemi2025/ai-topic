#!/usr/bin/env python3
"""Restore the exact bundled PDF into a caller-selected output location."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1] / 'assets' / 'reference-parts'
manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
data = b''.join((root / name).read_bytes() for name in manifest['parts'])
if len(data) != manifest['bytes'] or hashlib.sha256(data).hexdigest() != manifest['sha256']:
    raise SystemExit('Reference PDF integrity check failed.')
if args.output.exists():
    if args.output.read_bytes() != data:
        raise SystemExit('Output exists with different content; choose a new path.')
else:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(data)
print(f'PDF restored and verified: {args.output}')
