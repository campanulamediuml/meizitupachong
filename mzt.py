import requests

print requests.get(open('url_list.txt').readlines()[0].strip()).content
