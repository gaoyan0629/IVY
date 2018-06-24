from __future__ import print_function
import pandas as pd
import pathlib2 as Path
import config_json
import re

def file_loc(fn):
    f = Path.Path(config_json.get_search_home().get('search_home', Path.Path.home()))
    pattern = '{}.*'.format(re.split(r'\.', fn)[0])
    ret = list(f.rglob(pattern))
    cnt = len(ret)
    if cnt == 0:
        print('the file name [{}] not found'.format(fn))
        return
    elif cnt > 1:
        print('mutiple entry found [{}]'.format(ret))
        return
    return ret[0]


def load_dataset(fn):
    return pd.read_csv(file_loc(fn))
