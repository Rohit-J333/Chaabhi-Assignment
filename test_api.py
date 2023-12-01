import requests

# change it to api path on which api is being run
url = 'http://127.0.0.1:5000'
## to test api we can modify it

queries = []
queries.append("suggest me one product for bathing")
queries.append("what is price of chia seeds")
queries.append("what is most loved hair product")
queries.append("suggest one  Anti- Bacterial Scrub Pad")
queries.append("price of Soan Papdi Special")
queries.append("what is most loved beauty product")



for q in queries:

    data = {
        "question" : q
    }
    response = requests.post(url + "/test",json = data)
    if response.status_code == 200:
        result = response.json()["payload"]

        _ques = result["_ques"]
        _out = result["_out"]
        _sco = result["_sco"]
        _prod = result["_prod"]

        print(f"QUERY INPUT: {_ques}")
        print(f"OUTPUT: {_out} \nPREDICTION SCORE {_sco}\n\nReferred Product: {_prod}\n\n")

    else:
        print('Failed to fetch data:', response.status_code)








