# assert file exists
import os
# assert os.path.exists('mple.txt'), 'File not found!!'

# with open('sample.txt') as f:
#     content = f.read()
#     assert 'Hello Automation' in content, 'Content not found!!'
    
from pathlib import Path
p=Path('sample.txt')
print(p.parent)
print(p.suffix)
print(p.exists)