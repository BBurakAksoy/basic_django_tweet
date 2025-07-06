# Basic Django Tweet

A simple Twitter-like application built with Django, allowing users to post tweets, follow other users, and view a timeline of tweets from followed users.

## Features
- User authentication (register, login, logout)
- Post tweets with a character limit
- Follow/unfollow users
- View a personalized timeline of tweets from followed users
- Basic user profile page

## Requirements
- Python 3.8+
- Django 4.2+
- SQLite (default) or other supported database

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BBurakAksoy/basic_django_tweet.git
   cd basic_django_tweet
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage
- **Register**: Create a new account via the registration page.
- **Login**: Log in with your credentials to access the tweet functionality.
- **Post Tweets**: Share your thoughts in 280 characters or less.
- **Follow Users**: Follow other users to see their tweets in your timeline.
- **View Timeline**: Your homepage displays tweets from users you follow.

## Project Structure
- `tweets/`: Main app containing models, views, and templates for tweet functionality.
- `users/`: App handling user authentication and profiles.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files (CSS, JavaScript, etc.).

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Create a Pull Request.

## Contact
For questions or feedback, reach out to [BBurakAksoy](https://github.com/BBurakAksoy).