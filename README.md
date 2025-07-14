# From Pictures to Recipes - LLM Playground

This project is a FastAPI web application that allows users to interact with a Large Language Model (LLM) via a chat interface. Users can send text messages and upload images (such as food photos or guitar tabs), and the LLM will respond with relevant information or analysis. The app is designed as a playground for experimenting with LLM capabilities, including image and text processing.

## Features

- **Chat Interface:** Send text prompts and receive formatted LLM responses.
- **Image Upload:** Upload images to be analyzed or described by the LLM.
- **Markdown Formatting:** LLM responses are rendered with basic markdown support for better readability.
- **Responsive UI:** Built with Tailwind CSS for a modern look and feel.
- **Extensible Backend:** Easily swap out or extend the LLM and agent logic.

## Getting Started

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) or `pip`
- API keys for Google Generative AI (set via `set_enviroment`)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/danih02/from-pictures-to-recipes.git
    cd from-pictures-to-recipes
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Ensure your API keys are loaded via the `set_enviroment` module or a `.env` file.

4. **Run the app:**
    ```sh
    python main.py
    ```
    The app will be available at [http://localhost:8000](http://localhost:8000).

## Usage

- Open your browser and go to `http://localhost:8000`.
- Type a question or upload an image (or both) and click "Send".
- The chatbot will respond with a formatted answer.

## Project Structure

```
.
├── main.py                # FastAPI backend
├── image_message.py       # Helper for image+text message formatting
├── initialize_cooking_agent.py # LLM agent initialization
├── templates/
│   └── index.html         # Frontend UI (Jinja2 + Tailwind CSS)
├── static/                # Static files (if any)
└── requirements.txt       # Python dependencies
```

## Customization

- **LLM Model:** Change the model or parameters in `main.py` where `ChatGoogleGenerativeAI` is initialized.
- **Agent Logic:** Modify or extend `cooking_agent` in `initialize_cooking_agent.py`.
- **Frontend:** Edit `templates/index.html` for UI changes.

## License

MIT License

---

**Note:** This project is for educational and experimental purposes. For production use, review security and privacy considerations, especially regarding file uploads and API key management.
