import json
resp = """
{
    "url": "https://api.github.com/repos/torqata/oe-poet/pulls/332",
    "id": 910982608,
    "node_id": "PR_kwDOFbLOl842TH3Q",
    "html_url": "https://github.com/torqata/oe-poet/pull/332",
    "diff_url": "https://github.com/torqata/oe-poet/pull/332.diff",
    "patch_url": "https://github.com/torqata/oe-poet/pull/332.patch",
    "issue_url": "https://api.github.com/repos/torqata/oe-poet/issues/332",
    "number": 332,
    "state": "closed",
    "locked": false,
    "title": "Man 632 fix dag order and missing dags",
    "user": {
        "login": "brandon-braner",
        "id": 11854174,
        "node_id": "MDQ6VXNlcjExODU0MTc0",
        "avatar_url": "https://avatars.githubusercontent.com/u/11854174?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/brandon-braner",
        "html_url": "https://github.com/brandon-braner",
        "followers_url": "https://api.github.com/users/brandon-braner/followers",
        "following_url": "https://api.github.com/users/brandon-braner/following{/other_user}",
        "gists_url": "https://api.github.com/users/brandon-braner/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/brandon-braner/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/brandon-braner/subscriptions",
        "organizations_url": "https://api.github.com/users/brandon-braner/orgs",
        "repos_url": "https://api.github.com/users/brandon-braner/repos",
        "events_url": "https://api.github.com/users/brandon-braner/events{/privacy}",
        "received_events_url": "https://api.github.com/users/brandon-braner/received_events",
        "type": "User",
        "site_admin": false
    },
    "body": null,
    "created_at": "2022-04-15T17:09:41Z",
    "updated_at": "2022-04-16T05:19:43Z",
    "closed_at": "2022-04-16T05:19:43Z",
    "merged_at": "2022-04-16T05:19:43Z",
    "merge_commit_sha": "e8bfda8559d3b9b6fc34beed5744b0bb17cc818d",
    "assignee": null,
    "assignees": [],
    "requested_reviewers": [],
    "requested_teams": [],
    "labels": [],
    "milestone": null,
    "draft": false,
    "commits_url": "https://api.github.com/repos/torqata/oe-poet/pulls/332/commits",
    "review_comments_url": "https://api.github.com/repos/torqata/oe-poet/pulls/332/comments",
    "review_comment_url": "https://api.github.com/repos/torqata/oe-poet/pulls/comments{/number}",
    "comments_url": "https://api.github.com/repos/torqata/oe-poet/issues/332/comments",
    "statuses_url": "https://api.github.com/repos/torqata/oe-poet/statuses/19c09a39d3e1d92adba700b3ae3de238373d2d43",
    "head": {
        "label": "torqata:MAN-632-fix-dag-order-and-missing-dags",
        "ref": "MAN-632-fix-dag-order-and-missing-dags",
        "sha": "19c09a39d3e1d92adba700b3ae3de238373d2d43",
        "user": {
            "login": "torqata",
            "id": 68550328,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4NTUwMzI4",
            "avatar_url": "https://avatars.githubusercontent.com/u/68550328?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/torqata",
            "html_url": "https://github.com/torqata",
            "followers_url": "https://api.github.com/users/torqata/followers",
            "following_url": "https://api.github.com/users/torqata/following{/other_user}",
            "gists_url": "https://api.github.com/users/torqata/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/torqata/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/torqata/subscriptions",
            "organizations_url": "https://api.github.com/users/torqata/orgs",
            "repos_url": "https://api.github.com/users/torqata/repos",
            "events_url": "https://api.github.com/users/torqata/events{/privacy}",
            "received_events_url": "https://api.github.com/users/torqata/received_events",
            "type": "Organization",
            "site_admin": false
        },
        "repo": {
            "id": 364039831,
            "node_id": "MDEwOlJlcG9zaXRvcnkzNjQwMzk4MzE=",
            "name": "oe-poet",
            "full_name": "torqata/oe-poet",
            "private": true,
            "owner": {
                "login": "torqata",
                "id": 68550328,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4NTUwMzI4",
                "avatar_url": "https://avatars.githubusercontent.com/u/68550328?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/torqata",
                "html_url": "https://github.com/torqata",
                "followers_url": "https://api.github.com/users/torqata/followers",
                "following_url": "https://api.github.com/users/torqata/following{/other_user}",
                "gists_url": "https://api.github.com/users/torqata/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/torqata/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/torqata/subscriptions",
                "organizations_url": "https://api.github.com/users/torqata/orgs",
                "repos_url": "https://api.github.com/users/torqata/repos",
                "events_url": "https://api.github.com/users/torqata/events{/privacy}",
                "received_events_url": "https://api.github.com/users/torqata/received_events",
                "type": "Organization",
                "site_admin": false
            },
            "html_url": "https://github.com/torqata/oe-poet",
            "description": null,
            "fork": false,
            "url": "https://api.github.com/repos/torqata/oe-poet",
            "forks_url": "https://api.github.com/repos/torqata/oe-poet/forks",
            "keys_url": "https://api.github.com/repos/torqata/oe-poet/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/torqata/oe-poet/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/torqata/oe-poet/teams",
            "hooks_url": "https://api.github.com/repos/torqata/oe-poet/hooks",
            "issue_events_url": "https://api.github.com/repos/torqata/oe-poet/issues/events{/number}",
            "events_url": "https://api.github.com/repos/torqata/oe-poet/events",
            "assignees_url": "https://api.github.com/repos/torqata/oe-poet/assignees{/user}",
            "branches_url": "https://api.github.com/repos/torqata/oe-poet/branches{/branch}",
            "tags_url": "https://api.github.com/repos/torqata/oe-poet/tags",
            "blobs_url": "https://api.github.com/repos/torqata/oe-poet/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/torqata/oe-poet/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/torqata/oe-poet/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/torqata/oe-poet/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/torqata/oe-poet/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/torqata/oe-poet/languages",
            "stargazers_url": "https://api.github.com/repos/torqata/oe-poet/stargazers",
            "contributors_url": "https://api.github.com/repos/torqata/oe-poet/contributors",
            "subscribers_url": "https://api.github.com/repos/torqata/oe-poet/subscribers",
            "subscription_url": "https://api.github.com/repos/torqata/oe-poet/subscription",
            "commits_url": "https://api.github.com/repos/torqata/oe-poet/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/torqata/oe-poet/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/torqata/oe-poet/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/torqata/oe-poet/issues/comments{/number}",
            "contents_url": "https://api.github.com/repos/torqata/oe-poet/contents/{+path}",
            "compare_url": "https://api.github.com/repos/torqata/oe-poet/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/torqata/oe-poet/merges",
            "archive_url": "https://api.github.com/repos/torqata/oe-poet/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/torqata/oe-poet/downloads",
            "issues_url": "https://api.github.com/repos/torqata/oe-poet/issues{/number}",
            "pulls_url": "https://api.github.com/repos/torqata/oe-poet/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/torqata/oe-poet/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/torqata/oe-poet/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/torqata/oe-poet/labels{/name}",
            "releases_url": "https://api.github.com/repos/torqata/oe-poet/releases{/id}",
            "deployments_url": "https://api.github.com/repos/torqata/oe-poet/deployments",
            "created_at": "2021-05-03T19:32:48Z",
            "updated_at": "2021-12-30T16:12:02Z",
            "pushed_at": "2022-04-16T05:19:43Z",
            "git_url": "git://github.com/torqata/oe-poet.git",
            "ssh_url": "git@github.com:torqata/oe-poet.git",
            "clone_url": "https://github.com/torqata/oe-poet.git",
            "svn_url": "https://github.com/torqata/oe-poet",
            "homepage": null,
            "size": 3988,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "Python",
            "has_issues": true,
            "has_projects": true,
            "has_downloads": true,
            "has_wiki": true,
            "has_pages": false,
            "forks_count": 0,
            "mirror_url": null,
            "archived": false,
            "disabled": false,
            "open_issues_count": 8,
            "license": null,
            "allow_forking": true,
            "is_template": false,
            "topics": [],
            "visibility": "internal",
            "forks": 0,
            "open_issues": 8,
            "watchers": 0,
            "default_branch": "main"
        }
    },
    "base": {
        "label": "torqata:EPIC/MAN-632-yoy",
        "ref": "EPIC/MAN-632-yoy",
        "sha": "0d74d8618978ffae95e73edf2fa89e4bd9b8392f",
        "user": {
            "login": "torqata",
            "id": 68550328,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4NTUwMzI4",
            "avatar_url": "https://avatars.githubusercontent.com/u/68550328?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/torqata",
            "html_url": "https://github.com/torqata",
            "followers_url": "https://api.github.com/users/torqata/followers",
            "following_url": "https://api.github.com/users/torqata/following{/other_user}",
            "gists_url": "https://api.github.com/users/torqata/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/torqata/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/torqata/subscriptions",
            "organizations_url": "https://api.github.com/users/torqata/orgs",
            "repos_url": "https://api.github.com/users/torqata/repos",
            "events_url": "https://api.github.com/users/torqata/events{/privacy}",
            "received_events_url": "https://api.github.com/users/torqata/received_events",
            "type": "Organization",
            "site_admin": false
        },
        "repo": {
            "id": 364039831,
            "node_id": "MDEwOlJlcG9zaXRvcnkzNjQwMzk4MzE=",
            "name": "oe-poet",
            "full_name": "torqata/oe-poet",
            "private": true,
            "owner": {
                "login": "torqata",
                "id": 68550328,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4NTUwMzI4",
                "avatar_url": "https://avatars.githubusercontent.com/u/68550328?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/torqata",
                "html_url": "https://github.com/torqata",
                "followers_url": "https://api.github.com/users/torqata/followers",
                "following_url": "https://api.github.com/users/torqata/following{/other_user}",
                "gists_url": "https://api.github.com/users/torqata/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/torqata/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/torqata/subscriptions",
                "organizations_url": "https://api.github.com/users/torqata/orgs",
                "repos_url": "https://api.github.com/users/torqata/repos",
                "events_url": "https://api.github.com/users/torqata/events{/privacy}",
                "received_events_url": "https://api.github.com/users/torqata/received_events",
                "type": "Organization",
                "site_admin": false
            },
            "html_url": "https://github.com/torqata/oe-poet",
            "description": null,
            "fork": false,
            "url": "https://api.github.com/repos/torqata/oe-poet",
            "forks_url": "https://api.github.com/repos/torqata/oe-poet/forks",
            "keys_url": "https://api.github.com/repos/torqata/oe-poet/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/torqata/oe-poet/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/torqata/oe-poet/teams",
            "hooks_url": "https://api.github.com/repos/torqata/oe-poet/hooks",
            "issue_events_url": "https://api.github.com/repos/torqata/oe-poet/issues/events{/number}",
            "events_url": "https://api.github.com/repos/torqata/oe-poet/events",
            "assignees_url": "https://api.github.com/repos/torqata/oe-poet/assignees{/user}",
            "branches_url": "https://api.github.com/repos/torqata/oe-poet/branches{/branch}",
            "tags_url": "https://api.github.com/repos/torqata/oe-poet/tags",
            "blobs_url": "https://api.github.com/repos/torqata/oe-poet/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/torqata/oe-poet/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/torqata/oe-poet/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/torqata/oe-poet/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/torqata/oe-poet/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/torqata/oe-poet/languages",
            "stargazers_url": "https://api.github.com/repos/torqata/oe-poet/stargazers",
            "contributors_url": "https://api.github.com/repos/torqata/oe-poet/contributors",
            "subscribers_url": "https://api.github.com/repos/torqata/oe-poet/subscribers",
            "subscription_url": "https://api.github.com/repos/torqata/oe-poet/subscription",
            "commits_url": "https://api.github.com/repos/torqata/oe-poet/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/torqata/oe-poet/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/torqata/oe-poet/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/torqata/oe-poet/issues/comments{/number}",
            "contents_url": "https://api.github.com/repos/torqata/oe-poet/contents/{+path}",
            "compare_url": "https://api.github.com/repos/torqata/oe-poet/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/torqata/oe-poet/merges",
            "archive_url": "https://api.github.com/repos/torqata/oe-poet/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/torqata/oe-poet/downloads",
            "issues_url": "https://api.github.com/repos/torqata/oe-poet/issues{/number}",
            "pulls_url": "https://api.github.com/repos/torqata/oe-poet/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/torqata/oe-poet/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/torqata/oe-poet/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/torqata/oe-poet/labels{/name}",
            "releases_url": "https://api.github.com/repos/torqata/oe-poet/releases{/id}",
            "deployments_url": "https://api.github.com/repos/torqata/oe-poet/deployments",
            "created_at": "2021-05-03T19:32:48Z",
            "updated_at": "2021-12-30T16:12:02Z",
            "pushed_at": "2022-04-16T05:19:43Z",
            "git_url": "git://github.com/torqata/oe-poet.git",
            "ssh_url": "git@github.com:torqata/oe-poet.git",
            "clone_url": "https://github.com/torqata/oe-poet.git",
            "svn_url": "https://github.com/torqata/oe-poet",
            "homepage": null,
            "size": 3988,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "Python",
            "has_issues": true,
            "has_projects": true,
            "has_downloads": true,
            "has_wiki": true,
            "has_pages": false,
            "forks_count": 0,
            "mirror_url": null,
            "archived": false,
            "disabled": false,
            "open_issues_count": 8,
            "license": null,
            "allow_forking": true,
            "is_template": false,
            "topics": [],
            "visibility": "internal",
            "forks": 0,
            "open_issues": 8,
            "watchers": 0,
            "default_branch": "main"
        }
    },
    "_links": {
        "self": {
            "href": "https://api.github.com/repos/torqata/oe-poet/pulls/332"
        },
        "html": {
            "href": "https://github.com/torqata/oe-poet/pull/332"
        },
        "issue": {
            "href": "https://api.github.com/repos/torqata/oe-poet/issues/332"
        },
        "comments": {
            "href": "https://api.github.com/repos/torqata/oe-poet/issues/332/comments"
        },
        "review_comments": {
            "href": "https://api.github.com/repos/torqata/oe-poet/pulls/332/comments"
        },
        "review_comment": {
            "href": "https://api.github.com/repos/torqata/oe-poet/pulls/comments{/number}"
        },
        "commits": {
            "href": "https://api.github.com/repos/torqata/oe-poet/pulls/332/commits"
        },
        "statuses": {
            "href": "https://api.github.com/repos/torqata/oe-poet/statuses/19c09a39d3e1d92adba700b3ae3de238373d2d43"
        }
    },
    "author_association": "CONTRIBUTOR",
    "auto_merge": null,
    "active_lock_reason": null,
    "merged": true,
    "mergeable": null,
    "rebaseable": null,
    "mergeable_state": "unknown",
    "merged_by": {
        "login": "brandon-braner",
        "id": 11854174,
        "node_id": "MDQ6VXNlcjExODU0MTc0",
        "avatar_url": "https://avatars.githubusercontent.com/u/11854174?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/brandon-braner",
        "html_url": "https://github.com/brandon-braner",
        "followers_url": "https://api.github.com/users/brandon-braner/followers",
        "following_url": "https://api.github.com/users/brandon-braner/following{/other_user}",
        "gists_url": "https://api.github.com/users/brandon-braner/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/brandon-braner/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/brandon-braner/subscriptions",
        "organizations_url": "https://api.github.com/users/brandon-braner/orgs",
        "repos_url": "https://api.github.com/users/brandon-braner/repos",
        "events_url": "https://api.github.com/users/brandon-braner/events{/privacy}",
        "received_events_url": "https://api.github.com/users/brandon-braner/received_events",
        "type": "User",
        "site_admin": false
    },
    "comments": 0,
    "review_comments": 0,
    "maintainer_can_modify": false,
    "commits": 3,
    "additions": 9,
    "deletions": 9,
    "changed_files": 2
}
"""

resp = json.loads(resp)
print(resp['changed_files'])