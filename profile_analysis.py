import os
import sys
import json

def read_profile_data(file_path):
    data = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    if key in ['Followers', 'Followings', 'Posts']:
                        try:
                            value = int(value)
                        except ValueError:
                            print(f"Skipping line with non-integer value for {key}: {line}")
                            continue
                    data[key] = value
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error occurred while reading '{file_path}': {e}")
    return data

def analyze_profile(data):
    analysis = {
        'is_genuine': True,
        'reasons': []
    }

    # Check if the profile has a profile picture
    if 'Profile Picture URL' not in data:
        analysis['is_genuine'] = False
        analysis['reasons'].append("No profile picture.")

    # Check follower to following ratio
    followers = data.get('Followers', 0)
    following = data.get('Followings', 0)
    if following == 0 or followers / following < 0.1:
        analysis['is_genuine'] = False
        analysis['reasons'].append("Unusual followers to following ratio.")

    # Check bio description
    bio = data.get('Biography', "")
    if len(bio.strip()) == 0:
        analysis['is_genuine'] = False
        analysis['reasons'].append("No bio description.")

    # Check post count
    post_count = data.get('Posts', 0)
    if post_count < 10:
        analysis['is_genuine'] = False
        analysis['reasons'].append("Low post count.")

    return analysis

def main(username):
    profile_data_file = f'output/{username}.txt'
    if not os.path.exists(profile_data_file):
        print(f"Error: Profile data file '{profile_data_file}' does not exist.")
        return

    profile_data = read_profile_data(profile_data_file)
    if not profile_data:
        print("Error: No valid data found in profile data file.")
        return

    analysis = analyze_profile(profile_data)

    if analysis['is_genuine']:
        print("The profile appears to be genuine.")
    else:
        print("The profile appears to be fake for the following reasons:")
        for reason in analysis['reasons']:
            print(f"- {reason}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python profile_analysis.py <username>")
    else:
        username = sys.argv[1]
        main(username)
