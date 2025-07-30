# YouTubeStatistics

YouTubeStatistics is a Python script that automates the process of collecting analytics data from your YouTube channels. It runs as a web application using Flask and Docker, providing a simple interface for authorization and metrics selection.

## Features

- OAuth2 authentication with Google accounts  
- Selection of date ranges and metrics  
- Simple browser-based interface  
- Fully containerized using Docker

## Requirements

- Docker installed on your machine

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/YouTubeStatistics.git
   cd YouTubeStatistics
   ```

2. Set up your Google Cloud project:

   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Navigate to **APIs & Services > Library**
   - Search for and enable the following APIs:
     - **YouTube Data API v3**
     - **YouTube Analytics API**

3. Create OAuth credentials:

   - Navigate to **APIs & Services > Credentials**
   - Click **"Create Credentials"** → **"OAuth client ID"**
   - Choose **Web application** as the application type
   - Add the following authorized redirect URI:
     ```
     http://127.0.0.1:5555/google_auth_code_exchange
     ```
   - Download the JSON file with your credentials
   - Rename this file to `credentials.json` and place it in the root directory of the project (next to the Dockerfile)
   - **Important:** It may take a few minutes for the newly created credentials to become active and usable. Please wait before attempting authorization.
   - **Add your Google account to the list of test users:**  
     Go to **OAuth consent screen**, scroll to the **"Test users"** section, and add the email address of the Google account you plan to use for authentication.

4. Build the Docker image:

   ```bash
   docker build -t "ytstatistics" .
   ```

5. Run the container:

   ```bash
   docker run -p 5555:5555 --rm ytstatistics
   ```

6. Open the provided external link in your browser once the container is running.

## Using the Application

1. In the main menu, click **"Add Account"**.
2. Select the Google account with access to your YouTube channel.
3. Grant the requested permissions (read-only).
4. Once authorized, select your account from the **"Select Accounts"** dropdown.
5. Specify a start and end date.
6. Select the desired metrics to retrieve analytics data.

## Access

This project is currently in testing and access is restricted.

To request access, contact:

**gvazuk@gmail.com**












