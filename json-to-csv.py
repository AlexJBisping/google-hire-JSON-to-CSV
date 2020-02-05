import os
import re
import sys
import glob
import json
from pandas.io.json import json_normalize

directory_path = sys.argv[1]
json_file_paths = glob.glob('{}/*.json'.format(directory_path))
for json_file_path in json_file_paths:
    json_file_name = os.path.basename(json_file_path)
    do_not_parse = ['Integrations', 'Historical']
    if any(string in json_file_path for string in do_not_parse):
        continue
    print 'Processing {}...'.format(json_file_name)
    with open(json_file_path) as f:
        json_data = json.load(f)
    try:
        df = json_normalize(json_data)
    except:
        print('Could not process: {}'.format(json_file_name))
        continue
    csv_file_path = re.sub(".json", ".csv", json_file_path)
    df.to_csv(csv_file_path, index=False, encoding='utf-8')

