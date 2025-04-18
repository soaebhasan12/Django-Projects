# Number Guessing Game

This is a Django-based web application for a **Number Guessing Game**. The game allows users to guess a randomly generated number within a specific range, with two difficulty levels: **Easy** and **Hard**.

## Features

- **Home Page**: A welcoming page with a button to start the game.
- **Level Selection**: Choose between Easy and Hard difficulty levels.
- **Easy Level**: 10 attempts to guess the number between 1 and 100.
- **Hard Level**: 5 attempts to guess the number between 1 and 100.
- **Dynamic Feedback**: Provides feedback on whether the guessed number is too high or too low.
- **Game Over**: Displays a message when the user wins or loses.
- **Reset Game**: Option to reset the game and start over.

## Project Structure

```markdown
Num_Gue_Game/
│
├── db.sqlite3
├── manage.py
│
├── Num_Gue_Game/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── App_of_the_Game/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    │
    ├── migrations/
    │   └── __init__.py
    │
    ├── myTemplate/
    │   └── App_of_the_Game/
    │       ├── home.html
    │       ├── level.html
    │       ├── easy.html
    │       └── hard.html
    │
    └── static/
        └── images/
            ├── home.png
            ├── level.png
            ├── easy.png
            └── hard.png
```

## Installation

```markdown
   ```bash
1. Clone the repository:
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # For Windows
   ```

3. Install dependencies:
   ```bashs
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application:
   ```bash
   Open your browser and navigate to: http://127.0.0.1:8000/
   ```
```
```

## Usage

1. Navigate to the **Home Page**
2. Click on **"Play Game"** to proceed to the level selection page
3. Choose between **Easy** or **Hard** difficulty levels
4. Enter your guesses and follow the feedback provided
5. Reset the game or play again after winning or losing

   
## Technologies Used

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3
- **Database**: SQLite3
- **Development Tools**: Visual Studio Code, Git


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

- LinkedIn - [@Soaeb Hasan](https://www.linkedin.com/in/saibu-hassaa-789827360)
- Project Link: [https://github.com/soaebhasan12/Django-Projects/tree/main/Num_Gue_Game](https://github.com/soaebhasan12/Django-Projects/tree/main/Num_Gue_Game)

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/)
- [Font Awesome](https://fontawesome.com)
