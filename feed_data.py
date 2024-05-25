import requests
import sys

BASE_URL = "http://localhost:8000"

def create_user(user_id):
    url = f"{BASE_URL}/users/"
    data = {"user_id": user_id}
    response = requests.post(url, json=data)
    print(response.json())

def create_post(user_id, post_id):
    url = f"{BASE_URL}/posts/"
    data = {"user_id": user_id, "post_id": post_id}
    response = requests.post(url, json=data)
    print(response.json())

def create_liker(post_id, liker_id, name, title=None):
    url = f"{BASE_URL}/likers/"
    data = {"post_id": post_id, "liker_id": liker_id, "name": name, "title": title}
    response = requests.post(url, json=data)
    print(response.json())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python feed_data.py <command> [args]")
        print("Commands:")
        print("  create_user <user_id>")
        print("  create_post <user_id> <post_id>")
        print("  create_liker <post_id> <liker_id> <name> [title]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "create_user":
        if len(args) != 1:
            print("Usage: python feed_data.py create_user <user_id>")
            sys.exit(1)
        create_user(args[0])
    elif command == "create_post":
        if len(args) != 2:
            print("Usage: python feed_data.py create_post <user_id> <post_id>")
            sys.exit(1)
        create_post(args[0], args[1])
    elif command == "create_liker":
        if len(args) < 3:
            print("Usage: python feed_data.py create_liker <post_id> <liker_id> <name> [title]")
            sys.exit(1)
        title = None
        if len(args) == 4:
            title = args[3]
        create_liker(args[0], args[1], args[2], title)
    else:
        print("Invalid command")
        sys.exit(1)
        