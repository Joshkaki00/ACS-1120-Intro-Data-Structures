# Tweet Generator

This project is a simple tweet generator using a Markov chain. It leverages Flask for the backend, and HTML and Tailwind CSS for the frontend, to serve a web interface and API endpoints for generating sentences.

## Project Structure

- `app.py`: Main script that initializes the Flask application and Markov chain, and defines the routes.
- `markov.py`: Module containing functions to load the corpus, preprocess text, build the Markov chain, and generate sentences.
- `templates/index.html`: HTML template for the main page.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/(yourusername)/ACS-1120-Intro-Data-Structures.git
    cd ACS-1120-Intro-Data-Structures/Code
    ```
    **Replace *yourusername* with your actual username**

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare your corpus file:**
    Place your text file (e.g., `pg84-images.txt`) in the Code directory.

## Running the Application

To start the Flask server, run the following command in your terminal:
```bash
python app.py
```

By default, the server will run in port 5000. You can access the application at `http://127.0.0.1:5000/`.

## API Endpoints

- **Home Page (`/`):** Serves the main HTML page with a generated sentence.
- **Generate Sentence (`/generate`):** API endpoint that returns a new generated sentence.

## Example Usage

1. **Home Page:**
    - Visit `http://127.0.0.1:5000/` to see a generated sentence displayed on the main page.

2. **Generate Sentence:**
    - Visit `http://127.0.0.1:5000/generate` to get a new generated sentence in plain text.

## Notes

- Ensure your corpus file is properly formatted and placed in the project directory.
- Adjust the `FILENAME` and `SENTENCE_LENGTH` variables in `app.py` as needed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
