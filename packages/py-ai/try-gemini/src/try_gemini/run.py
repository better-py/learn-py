import google.generativeai as genai
import typer
from loguru import logger

app = typer.Typer()


@app.command()
def run(api_key: str):
    if not api_key:
        logger.error("Please set the GOOGLE_GEMINI_API_KEY environment variable.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content("The opposite of hot is")
    logger.info(f"response: {response.text}")  # cold.


if __name__ == '__main__':
    typer.run(run)
