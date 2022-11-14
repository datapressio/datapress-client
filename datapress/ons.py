def get_all_datasets():
    # Returns all the datasets available on the ONS API. Also goes and fetches the latest download link (ie most recent version) and the geographic resolution.
    import requests
    datasets = []
    api_result = {
        'items': []
    }
    # keep hitting the ONS API and appending the data to the array
    limit = 1000
    while len(api_result['items']) == limit or len(datasets) == 0:
        api_result = requests.get(
            'https://api.beta.ons.gov.uk/v1/datasets?limit=' + str(limit) + '&offset=' + str(len(datasets))).json()
        datasets += (api_result['items'])

    # embellish the datasets with extra data
    for dataset in datasets:
        url = dataset['links']['latest_version']['href']
        dataset_api_result = requests.get(url).json()
        if 'downloads' in dataset_api_result.keys():
            if 'csv' in dataset_api_result['downloads'].keys():
                dataset['download'] = dataset_api_result['downloads']['csv']['href']
            elif 'xls' in dataset_api_result['downloads'].keys():
                dataset['download'] = dataset_api_result['downloads']['xls']['href']
        dataset['dimensions'] = dataset_api_result['dimensions']
        for dimension in dataset['dimensions']:
            if (dimension['name'] == 'geography'):
                dataset['geography'] = dimension['id']

    return datasets


def get_ons_dataset(id, filters):
    # fetches a dataset from the ONS API, and returns a pandas dataframe, with the filters applied
    import requests
    import pandas as pd

    dataset_url = "https://api.beta.ons.gov.uk/v1/datasets/" + id
    dataset_metadata = requests.get(dataset_url).json()
    latest_version = dataset_metadata['links']['latest_version']['href']
    data_url = latest_version + "/observations?"
    for key in filters.keys():
        data_url += key + "=" + str(filters[key]) + "&"
    dataset = requests.get(data_url).json()
    df = pd.json_normalize(dataset['observations'])

    good_columns = ['observation']
    for col in df.columns:
        bits = col.split('.')
        if bits[-1] == 'label':
            df = df.rename(columns={col: bits[1]})
            good_columns.append(bits[1])
    df = df[good_columns]
    df = df.rename(columns={"observation": dataset['unit_of_measure']})
    return df
