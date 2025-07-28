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

2. Build the Docker image:

   ```bash
   docker build -t "ytstatistics" .
   ```

3. Run the container:

   ```bash
   docker run -p 5555:5555 --rm ytstatistics
   ```

4. Open the provided external link in your browser once the container is running.

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





