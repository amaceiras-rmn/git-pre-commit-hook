"""Check that files contains valid JSON."""
import os
import fnmatch
import json


DEFAULTS = {
    'files': '*.json',
}

def check(file_staged_for_commit, options):
    basename = os.path.basename(file_staged_for_commit.path)
    if not fnmatch.fnmatch(basename, options.json_files):
        return True
    try:
        path, ext = os.path.splitext(file_staged_for_commit.path)
        idx = path.find("/project/")
        if idx == -1:
            return True
        path = path[idx + len("/project/"):]
        path = path.replace("/", ".")
        content = json.loads(file_staged_for_commit.contents)
        title = content['title']
        assert path == title
    except:
        return False
    else:
        return True
