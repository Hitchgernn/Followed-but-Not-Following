import json
import unicodedata

def load_usernames_following(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        usernames = set()

        if isinstance(data, dict) and "relationships_following" in data:
            data = data["relationships_following"]

        for entry in data:
            if "string_list_data" in entry:
                for user in entry["string_list_data"]:
                    usernames.add(user["value"])

        return usernames

def load_usernames_followers(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        usernames = set()
        for entry in data:
            if "string_list_data" in entry:
                for user in entry["string_list_data"]:
                    usernames.add(user["value"])

        return usernames

def find_unfollowers(followers_file, following_file):
    # the structure of these two json files are different so i gotta separate the code
    followers = load_usernames_followers(followers_file)
    following = load_usernames_following(following_file)

    print(f"Total Followers: {len(followers)}")
    print(f"Total Following: {len(following)}")

    unfollowers = following - followers
    return unfollowers

def display_results(unfollowers):
    if unfollowers:
        print("People who don't follow you back:")
        for user in sorted(unfollowers):
            print(f"- {user}")
    else:
        print("\nEveryone you follow also follows you back!")

if __name__ == "__main__":
    followers_file = "followers.json"
    following_file = "following.json"

    unfollowers = find_unfollowers(followers_file, following_file)
    display_results(unfollowers)
