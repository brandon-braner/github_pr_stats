Steps

* get all repos
* for each repo get each pull request
* for each pull request get:
* - time date submitted
* - time date merged
* - delta between submitted and merged
* - number of comments 
* - time and date of each approval and by whom
- for each approval: track who approved and how long it takes



endpoints

## get all repos
https://api.github.com/orgs/torqata/repos

## get all pull requests
https://api.github.com/repos/torqata/{repos}/pulls


## get pull request times
https://api.github.com/repos/torqata/{repo}/issues/{pr-id}/timeline

https://api.github.com/repos/torqata/oe-poet/pulls/332
- number of files changed : changed_files
- comment count : comments
