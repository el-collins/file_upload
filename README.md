# UserProfile FastAPI Service

## Overview
This service provides an API for creating and retrieving user profiles, including uploading and saving profile pictures.

## Features
- Create user profiles with username, phone number, email, and profile picture.
- Retrieve user profiles by ID.
- Profile pictures are saved to disk.
- User-Agent header is captured and returned with responses.

## Tech Stack
- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **SQLModel**: For interacting with the database using SQL and Python models.
- **Shutil**: For handling file operations.

## Installation

To get started with this project, clone the repository and install the required packages.

```bash
git clone https://your-repository-url
cd your-project-directory
poetry shell
poetry install
```

## Usage

Run the FastAPI server with the following command:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### Create Profile

`POST /profiles/`

Creates a new user profile with the provided username, phone number, email, and profile picture.

#### Parameters:
- `username`: The username of the user.
- `phone_number`: The phone number of the user.
- `email`: The email address of the user.
- `profile_picture`: The profile picture file.

#### Responses:
- `200 OK`: Profile created successfully.
- `400 Bad Request`: Error occurred during profile creation.

### Get Profile

`GET /profiles/{profile_id}`

Retrieves the user profile with the specified ID.

#### Parameters:
- `profile_id`: The unique identifier of the user profile.

#### Responses:
- `200 OK`: Profile retrieved successfully.
- `404 Not Found`: Profile not found.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the MIT license.


Remember to replace `https://your-repository-url` and `your-project-directory` with the actual URL and directory name of your project. 