import requests
import json

headers = {
"Authorization": "Bearer 6a9180930feb1ad02c1d24fc4a6a9dd13f37237b", 
"User-Agent": "allenmiao"
}

def run_query(query): 
	request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
	if request.status_code == 200:
		return request.json()
	else:
		raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

find_pr_id_query = """
query FindPullRequestID {
  repository(owner: "%s", name: "%s") {
    pullRequest(number: %d) {
      id
    }
  }
}""" % ("sophaz", "gitpractice", 9) # provide your arguments here to the query string

# Execute the query, get the pull request ID
pull_request_id_data = run_query(find_pr_id_query) 
pull_request_id = pull_request_id_data["data"]["repository"]["pullRequest"]["id"]
print("Pull request id is " + pull_request_id)

"""
Docs here:
https://developer.github.com/v4/mutation/addpullrequestreview/

pullRequestId is the only required parameter. You can provide additional, optional parameters:
	- body
	- comments
	- clientMutationId : unique identifier for the client performing the mutation
	- commitOID : The commit OID the review pertains to
	- event: The event to perform on the pull request review (accept, comment, dismiss, or request changes)
"""

add_review_get_id_mutation = """
mutation addReviewAndGetID {
  addPullRequestReview(input: {
    body: "%s", 
    pullRequestId: "%s"}
  ) {
    pullRequestReview {
      id
    }
  }
}
""" % ("Creating a new review from Python!", pull_request_id)

# Execute the mutation, get the pull request review ID
pull_request_review_id_data = run_query(add_review_get_id_mutation) 
pull_request_review_id = pull_request_review_id_data["data"]["addPullRequestReview"]["pullRequestReview"]["id"]
print("Created a review. The review id is " + pull_request_review_id)

"""
Docs here:
https://developer.github.com/v4/mutation/addpullrequestreviewcomment/

pullRequestId is the only required parameter. You can provide additional, optional parameters:
	- body
	- inReplyTo: The comment id to reply to.
	- path: The relative path of the file to comment on.
	- position: The line index in the diff to comment on.
	- clientMutationId : unique identifier for the client performing the mutation
	- commitOID : The commit OID the review pertains to

If you don't provide a a path/positon, the comment just goes into the conversation thread in the PR. 
"""

add_comment_mutation = """
mutation AddPullRequestComment {
  addPullRequestReviewComment(input: {
    pullRequestReviewId: "%s", 
    body: "%s", 
    path: "%s", 
    position: %d}) {
    comment {
      id,
      author {
        login
      }
      body,
      path,
      position
    }
  }
}
""" % (pull_request_review_id, "Here is a comment from Python!", "test_file.swift", 30) # provide your arguments here for body, path, and line #

# Execute the mutation, get the payload and print it
add_comment_data = run_query(add_comment_mutation) 
print("Added a comment. Here is the payload: " + json.dumps(add_comment_data, indent=2))
