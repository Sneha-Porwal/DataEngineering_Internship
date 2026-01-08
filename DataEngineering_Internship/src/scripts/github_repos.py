from src.common.api_client import get_json

URL = "https://api.github.com/users/Sneha-Porwal/repos"

def main():
    repos = get_json(URL)
    for repo in repos:
        print("Repository:", repo["name"])


if __name__ == "__main__":
    main()
