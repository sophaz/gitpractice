curl -X POST \
  https://api.github.com/graphql \
  -H 'Authorization: bearer d068968d498fee66aa8599c0f76e151c552c8084' \
  -H 'Content-Type: application/json' \
  -d '{"query": "mutation { addComment(input:{clientMutationId: \"1234\", subjectId: \"MDExOlB1bGxSZXF1ZXN0MjE2MTUwMzk4\", body: \"Looks good to me again from CircleCI\"}) { clientMutationId commentEdge {node {body      }}}}" }'
