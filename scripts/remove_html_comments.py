import re
import glob
import os
import sys

COMMENT_RE = re.compile(r'<!--.*?-->', re.DOTALL)

root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rip')
pattern = os.path.join(root, '**', '*.html')

files = glob.glob(pattern, recursive=True)
scanned = 0
modified = 0
total_removed = 0

for filepath in files:
    scanned += 1
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except Exception as e:
        print(f'  SKIP (read error): {filepath} — {e}', file=sys.stderr)
        continue

    new_content, count = COMMENT_RE.subn('', content)
    if count:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified += 1
        total_removed += count

print(f'Scanned : {scanned} files')
print(f'Modified: {modified} files')
print(f'Comments removed: {total_removed}')
