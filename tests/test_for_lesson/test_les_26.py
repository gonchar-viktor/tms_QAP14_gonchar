import requests

#response = requests.get('https://jsonplaceholder.typicode.com/posts/68')
#json = response.json()

#assert json['title'] == 'laboriosam dolor voluptates', 'Test failed'


#Body, title, id and userId

def test_id():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/68')
    val = response.json()

    assert val['id'] == 68


    assert val['body'] == 'magnam molestiae perferendis quisquam\nqui ' \
                               'cum reiciendis\nquaerat animi amet hic inven' \
                               'tore\nea quia deleniti quidem saepe porro ve' \
                               'lit'

    assert val['userId'] == 7


    assert val['title'] == 'odio quis facere architecto reiciendis ' \
                                  'optio'