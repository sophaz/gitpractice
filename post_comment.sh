curl -X POST \
  https://api.github.com/graphql \
  -H 'Authorization: bearer 3747a4fc143b98169d443329b152e0a9f2daacfa' \
  -H 'Content-Type: application/json' \
  -d '{"query": "mutation { addComment(input:{clientMutationId: \"1234\", subjectId: \"MDExOlB1bGxSZXF1ZXN0MjE2MTUwMzk4\", body: \"Looks good to me again from CircleCI\"}) { clientMutationId commentEdge {node {body      }}}}" }'
