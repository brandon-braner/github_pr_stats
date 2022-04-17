from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

import requests
import aiohttp
from .utils.url_utils import get_query_string_value


class PyGithub:

    def __init__(self, user: str, token: str):
        """Pass in the GitHub user and personal access token."""
        self.base_url = "https://api.github.com"
        self.user = user
        self.token = token

    def get_repos(self) -> list:
        # TODO: self.user for org may need to be different then user
        url = f"{self.base_url}/orgs/{self.user}/repos?per_page=100"
        response = requests.get(url, auth=(self.user, self.token))
        # if response.status_code != 200:
        #     raise Exception(f"Error: {response.status_code}")

        # see if there are extra pages to get
        repos = list(response.json())
        if response.links.get("last"):
            number_of_pages = get_query_string_value(response.links["last"]["url"], "page")
            for page in range(2, int(number_of_pages) + 1):
                response = requests.get(f"{url}&page={page}", auth=(self.user, self.token))
                # if response.status_code != 200:
                #     raise Exception(f"Error: {response.status_code}")
                response_json = response.json()
                repos.extend(list(response_json))

        return repos

    def get_repo_pull_requests(self, repo_full_name: str, state: str, length_in_months: int) -> list:
        """Get Pull Requests for a repo in a specific status going back x amount of months."""
        url = f"{self.base_url}/repos/{repo_full_name}/pulls"
        response = requests.get(f"{url}", auth=(self.user, self.token))
        pr = response.json()
        # if pr is empty or if the state does not match return empty list


        open_date = datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ').date()
        current_date = date.today()
        max_pr_open_date = current_date - relativedelta(months=length_in_months)
        # return an empty list so len check passes
        # if open_date < max_pr_open_date:
            # return []

        return pr
