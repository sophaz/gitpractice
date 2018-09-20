from urlparse import urlparse
from urlrequest import urlrequest

url = 'https://api.github.com/graphql'
post_fields = {'query': '{"query": "query { repository(owner:\"octocat\", name:\"Hello-World\") { id } }"}'}

request = Request(url, urlencode(post_fields).encode())
request.add_header('Authorization', 'bearer 2ac3e0d1786589fba0d90212068536514673ded5')
json = urlopen(request).read().decode()
print(json)
