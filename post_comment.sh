curl -X POST \
 -H "Authorization: bearer ${CIRCLE_API_PROJECT_TOKEN}" \
 -H 'Content-Type: application/json' \
 -d '{"query": "mutation { addComment(input:{clientMutationId: \"1234\", subjectId: \"MDExOlB1bGxSZXF1ZXN0MjE2MTUwMzk4\", body: \"Looks good to me again from CircleCI\"}) { clientMutationId commentEdge {node {body }}}}" }' \
 https://api.github.com/graphql
