import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def display_activity(events):
    for event in events:
        event_type = event['type']
        repo_name = event['repo']['name']
        if event_type == 'PushEvent':
            commits = len(event['payload']['commits'])
            print(f"Pushed {commits} commits to {repo_name}")
        elif event_type == 'IssuesEvent':
            action = event['payload']['action']
            print(f"{action.capitalize()} an issue in {repo_name}")
        elif event_type == 'WatchEvent':
            print(f"Starred {repo_name}")
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: github_activity <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    events = fetch_github_activity(username)
    if events:
        display_activity(events)
