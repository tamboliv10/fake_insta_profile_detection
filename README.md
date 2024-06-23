# FAKE USER PROFILE IDENTIFICATION SYSTEM USING ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING

## Project Description:

This is a Python-based tool designed to evaluate the authenticity of Instagram profiles, addressing the increasing issue of fake accounts on social media. Utilizing the instaloader library, InstaVerified extracts comprehensive profile data and analyzes it against predefined criteria to determine if a profile is likely genuine or fake.
The tool focuses on key indicators such as the presence of a profile picture, follower-to-following ratio, bio description, and post count to assess profile authenticity. While currently serving as a basic prototype, InstaVerified sets the foundation for future enhancements, including analysis of comments, captions, and the nature of the user's followers.


## Features
User Profile Information Analysis: Input various profile attributes to determine if the account is fake or real.

## Requirements
- joblib==1.3.2
- numpy==1.26.4
- pandas==2.2.2
- scikit_learn==1.3.2
- tensorflow==2.15.0
- tensorflow_intel==2.15.0

## Installation:

### 1. Clone the repository:

    git clone https://github.com/tamboliv10/fake_insta_profile_detection.git
    cd fake-user-profile-identification

### 2. Create a virtual environment:

    python -m venv venv
    source venv/bin/activate    # On Windows, use `venv\Scripts\activate`

### 3. Install the required packages:

    pip install -r requirements.txt

Ensure requirements.txt contains the following:

- Flask==3.0.3
- joblib==1.3.2
- numpy==1.26.4
- pandas==2.2.2
- scikit_learn==1.3.2
- tensorflow==2.15.0
- tensorflow_intel==2.15.0
