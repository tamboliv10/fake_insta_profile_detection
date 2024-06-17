import instaloader
import os
import sys

loader = instaloader.Instaloader()


def save_profile_data(profile, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, f'{profile.username}.txt')

    with open(file_path, 'w') as file:
        file.write(f"Username: {profile.username}\n")
        file.write(f"ID: {profile.userid}\n")
        file.write(f"Name: {profile.full_name}\n")
        file.write(f"Biography: {profile.biography}\n")

        # List external URLs
        external_urls = [profile.external_url] if profile.external_url else []
        file.write(f"External URLs:\n")
        for url in external_urls:
            file.write(f" - {url}\n")

        file.write(f"Followings: {profile.followees}\n")
        file.write(f"Followers: {profile.followers}\n")
        file.write(f"Blocked by User: {profile.blocked_by_viewer}\n")
        file.write(f"Highlight Reels: {profile.has_highlight_reels}\n")
        file.write(f"Public Story: {profile.has_public_story}\n")
        file.write(f"IGTV: {profile.igtvcount}\n")
        file.write(f"Business Account: {profile.is_business_account}\n")
        file.write(f"Private Account: {profile.is_private}\n")
        file.write(f"Verified: {profile.is_verified}\n")
        file.write(f"Posts: {profile.mediacount}\n")
        file.write(f"Profile Picture URL: {profile.profile_pic_url}\n")


def save_comments(post, directory, profile_username):
    comments_dir = os.path.join(directory, 'comments')
    if not os.path.exists(comments_dir):
        os.makedirs(comments_dir)

    post_filename = os.path.join(comments_dir, f'{profile_username}_{post.date}.txt')

    with open(post_filename, 'w') as file:
        file.write(f"Post URL: {post.url}\n")
        file.write(f"Date: {post.date}\n")
        file.write(f"Likes: {post.likes}\n")
        file.write(f"Comments:\n")
        for comment in post.get_comments():
            file.write(f" - {comment.owner.username}: {comment.text}\n")


def fetch_full_profile(username, output_dir):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        save_profile_data(profile, output_dir)

        # Fetch and save comments from all posts
        posts_dir = os.path.join(output_dir, 'posts')
        if not os.path.exists(posts_dir):
            os.makedirs(posts_dir)

        for post in profile.get_posts():
            save_comments(post, posts_dir, username)

        print(f"\033[32mFull profile and comments saved to {output_dir}/{profile.username}.txt and {posts_dir}\033[0m")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"\033[33mProfile '{username}' not found.\033[0m")
    except Exception as e:
        print(f"\033[31mAn error occurred while fetching '{username}': {e}\033[0m")


def fetch_profile(username, output_dir):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        save_profile_data(profile, output_dir)
        print(f"\033[32mBasic profile data saved to {output_dir}/{profile.username}.txt\033[0m")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"\033[33mProfile '{username}' not found.\033[0m")
    except Exception as e:
        print(f"\033[31mAn error occurred while fetching '{username}': {e}\033[0m")


def check_follow_status(loader, username, target_username):
    try:
        profile = instaloader.Profile.from_username(loader.context, target_username)
        followers = profile.get_followers()
        if any(follower.username == username for follower in followers):
            return True
        else:
            return False
    except Exception as e:
        print(f"\033[31mAn error occurred while checking follow status: {e}\033[0m")
        return False


def main():
    output_dir = 'output'

    # Get credentials
    username = input("\033[36mEnter your Instagram username: \033[0m")
    password = input("\033[36mEnter your Instagram password: \033[0m")

    # Login
    try:
        loader.load_session_from_file(username)
    except FileNotFoundError:
        try:
            loader.login(username, password)
            loader.save_session_to_file()
            print(f"\033[32mLogged in as {username}\033[0m")
        except Exception as e:
            print(f"\033[31mFailed to log in: {e}\033[0m")
            sys.exit()

    # Get target username
    target_username = input("\033[36mEnter the username of the profile to fetch: \033[0m")

    if target_username == "":
        print("\033[33mUnknown command!\033[0m")
        sys.exit()

    if check_follow_status(loader, username, target_username):
        fetch_full_profile(target_username, output_dir)
    else:
        print(f"\033[33mYou do not follow {target_username}. Displaying basic profile details.\033[0m")
        fetch_profile(target_username, output_dir)


if __name__ == "__main__":
    main()
