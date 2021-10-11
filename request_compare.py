import json
import requests

def call_SSR_CTI(data, headers):
    url = 'https://virtual-cti-ai-services-ssr-python3-test.ctis.staging-backend-20200624.eks.compass.com/api/v3/searchsuggestranker'
    token = 'Bearer <INSERT_remember_TOKEN_From_CTI>'
    headers["authorization"] = token
    print("------call_SSR_CTI------")
    return requests.post(url, json=data, headers=headers, verify=False)


def call_SSR_staging(data, headers):
    url = 'https://staging.compass.com/api/v3/searchsuggestranker'
    token = 'Bearer <INSERT_staging_remember_TOKEN>'
    headers["authorization"] = token
    print("------call_SSR_staging------")
    return requests.post(url, json=data, headers=headers)

def isResponseSame(data):
    headers1 = {"content-type": "application/json"}
    call1 = call_SSR_CTI(data, headers1)
    json1 = json.dumps(call1.json(), sort_keys=True)
    print(json1)

    call2 = call_SSR_staging(data, headers1)
    json2 = json.dumps(call2.json(), sort_keys=True)
    print(json2)
    return call1.json()["categoryPredictions"] == call2.json()["categoryPredictions"] and call1.json()["suggestionPredictions"] == call2.json()["suggestionPredictions"]



def test_sample_requests():
    test_requests = []
    test_requests.append('''{"metadata":{"attemptId":"bef1bcc7-4b18-4da8-87c3-19567b3056ba","businessId":null,"correlationId":null,"timestamp":"2021-06-25T22:18:34.310Z","userType":null,"isMobileApp":false,"setBusinessId":false,"setTimestamp":true,"setCorrelationId":false,"setUserType":false,"setAttemptId":true,"setIsMobileApp":false},"data":{"queryData":{"query":"test","ucGeoId":null,"activeTokens":null,"geoLocation":null,"activeTokensSize":0,"activeTokensIterator":null,"setActiveTokens":false,"setGeoLocation":false,"setUcGeoId":false,"setQuery":true},"suggestionsToRank":[{"category":"STREET","ucGeoId":"long_island","id":"Test","source":"STREET","suggestionText":"Test","listingSuggestionInfo":null,"categoryLabel":"Streets","multipleListingSuggestionInfo":null,"setSuggestionText":true,"setListingSuggestionInfo":false,"setCategoryLabel":true,"setMultipleListingSuggestionInfo":false,"setUcGeoId":true,"setSource":true,"setId":true,"setCategory":true},{"category":"AGENT_NAME","ucGeoId":null,"id":"AGENT_NAME_FREE_TEXT:test","source":"AGENT_NAME_FREE_TEXT","suggestionText":"test","listingSuggestionInfo":null,"categoryLabel":"Agent Name Search","multipleListingSuggestionInfo":null,"setSuggestionText":true,"setListingSuggestionInfo":false,"setCategoryLabel":true,"setMultipleListingSuggestionInfo":false,"setUcGeoId":false,"setSource":true,"setId":true,"setCategory":true},{"category":"SCHOOL","ucGeoId":"westchester_ny","id":"250732","source":"SCHOOL","suggestionText":"New Testament Church School","listingSuggestionInfo":null,"categoryLabel":"Schools","multipleListingSuggestionInfo":null,"setSuggestionText":true,"setListingSuggestionInfo":false,"setCategoryLabel":true,"setMultipleListingSuggestionInfo":false,"setUcGeoId":true,"setSource":true,"setId":true,"setCategory":true}],"categoriesToRank":[{"category":"STREET","label":"Streets","setLabel":true,"setCategory":true},{"category":"AGENT_NAME","label":"Agent Name Search","setLabel":true,"setCategory":true},{"category":"SCHOOL","label":"Schools","setLabel":true,"setCategory":true}],"setQueryData":true,"suggestionsToRankSize":3,"suggestionsToRankIterator":[{"category":"STREET","ucGeoId":"long_island","id":"Test","source":"STREET","suggestionText":"Test","listingSuggestionInfo":null,"categoryLabel":"Streets","multipleListingSuggestionInfo":null,"setSuggestionText":true,"setListingSuggestionInfo":false,"setCategoryLabel":true,"setMultipleListingSuggestionInfo":false,"setUcGeoId":true,"setSource":true,"setId":true,"setCategory":true},{"category":"AGENT_NAME","ucGeoId":null,"id":"AGENT_NAME_FREE_TEXT:test","source":"AGENT_NAME_FREE_TEXT","suggestionText":"test","listingSuggestionInfo":null,"categoryLabel":"Agent Name Search","multipleListingSuggestionInfo":null,"setSuggestionText":true,"setListingSuggestionInfo":false,"setCategoryLabel":true,"setMultipleListingSuggestionInfo":false,"setUcGeoId":false,"setSource":true,"setId":true,"setCategory":true},{"category":"SCHOOL","ucGeoId":"westchester_ny","id":"250732","source":"SCHOOL","suggestionText":"New Testament Church School","listingSuggestionInfo":null,"categoryLabel":"Schools","multipleListingSuggestionInfo":null,"setSuggestionText":true,"setListingSuggestionInfo":false,"setCategoryLabel":true,"setMultipleListingSuggestionInfo":false,"setUcGeoId":true,"setSource":true,"setId":true,"setCategory":true}],"setSuggestionsToRank":true,"categoriesToRankSize":3,"categoriesToRankIterator":[{"category":"STREET","label":"Streets","setLabel":true,"setCategory":true},{"category":"AGENT_NAME","label":"Agent Name Search","setLabel":true,"setCategory":true},{"category":"SCHOOL","label":"Schools","setLabel":true,"setCategory":true}],"setCategoriesToRank":true},"hyperparameters":{"categoryLimit":0,"categoryThreshold":0.0,"suggestionLimit":14,"suggestionThreshold":0.0,"setCategoryLimit":false,"setCategoryThreshold":false,"setSuggestionLimit":true,"setSuggestionThreshold":false},"apiVersion":"v4.3","setApiVersion":true,"setData":true,"setHyperparameters":true,"setMetadata":true}''')

    for req in test_requests:
        parsed_req = json.loads(req)
        print(isResponseSame(parsed_req))

test_sample_requests()

