import requests

def url(path):
    return 'http://34.207.10.230:3000' + path


def view_feed():
    resp = requests.get(url('/posts'))
    print(resp.content)


def post_news(title, body):
    return requests.post(url('/posts'), json={
        'title': title,
        'body': body
    })


def comment(postId, body):
    return requests.post(url('/comments'), json={
        "body": body,
        "postId": postId
    })


comment(ByHiXBVd,"Endiro")
