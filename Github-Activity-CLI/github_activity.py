import sys
import requests


def fetch_github_activity(username):
    print(f"Fetching Github activity for {username}...")
    
    activity_fetch_url = f"https://api.github.com/users/{username}/events"

    try:
        response = requests.get(activity_fetch_url)
        response.raise_for_status() 
        activities = response.json()

        if  not activities:
            print(f"No Github activity found for {username}")
            return

        for activity in activities:
            activity_type = activity['type']
            repo_name = activity['repo']['name']

            if activity_type == 'PushEvent':
                commit_count = len(activity['payload']['commits'])
                print(f"Pushed {commit_count} commits to {repo_name}")
                
            elif activity_type == 'IssueEvent':
                action = activity['payload']['action']
                print(f"{action.capitalize()} issue on {repo_name}")
            
            elif activity_type == 'WatchEvent':
                print(f"Starred {repo_name}")
            
            else:
                print(f"Performed {activity_type} on {repo_name}")

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f"Github user {username} not found!")
        else:
            print(f"Failed to fetch Github activity for {username}! Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Failed to fetch Github activity for {username}! Error: {err}")
    except Exception as err:
        print(f"An error occurred while fetching Github activity for {username}! Error: {err}")


def main():
    if len(sys.argv) != 2:
        print("Usage: github_activity.py <github_username>")
        return
    
    username = sys.argv[1]
    fetch_github_activity(username)

if __name__ == '__main__':
    main()