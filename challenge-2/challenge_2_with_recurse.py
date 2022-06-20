import requests
import json
from nested_lookup import nested_lookup

metadata_url = "http://169.254.169.254/latest/meta-data/"
#metadata_url = "http://169.254.169.254/latest/meta-data/block-device-mapping/"
#metadata_url = "http://169.254.169.254/latest/meta-data/events/"


def Get_JSON_Metadata(url):

    temp_output = {}
    temp = {}
    response = requests.get(url).text

    if(url.endswith('/')):
        metadata_list = response.splitlines()
        for metadata in metadata_list:
            temp_url = url + metadata
            temp.update(Get_JSON_Metadata(temp_url))
        temp_output[url.rsplit('/')[-2]] = temp
    elif(response.startswith('{') and response.endswith('}')):
        temp_output[url.rsplit('/')[-1]] = json.loads(response)
    else:
        temp_output[url.rsplit('/')[-1]] = response

    return temp_output



output_json = Get_JSON_Metadata(metadata_url)
print(json.dumps(output_json, indent=2, default=str, sort_keys=True))

key = input('Enter your key: ')
print(nested_lookup(key, output_json))
