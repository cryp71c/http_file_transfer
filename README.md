# Simple Python HTTP Server with File Upload

This is a simple Python HTTP server that can handle file uploads via POST requests. The server listens on a specified IP address and port and saves the uploaded files to the server's working directory.

## Features

- **File Uploads:** Handles HTTP POST requests to upload files.
- **Customizable Server:** Allows you to specify the local IP address and port for the server.

## How It Works

1. **POST Request Handling:**
   - The server reads the incoming POST data and saves it as a file in the working directory.
   - The file is saved with the same name as the path provided in the request.

2. **Response:**
   - After saving the file, the server responds with a `200 OK` status and a success message.

## Prerequisites

- Python 3.x

## Usage

### Running the Server

You can run the server with the following command:

```bash
python3 server.py -l <LOCAL_IP> -p <PORT>
