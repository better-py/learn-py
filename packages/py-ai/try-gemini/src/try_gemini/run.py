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

    # usage 1:
    response = model.generate_content("The opposite of hot is")
    logger.info(f"response: {response.text}")  # cold.

    # usage 2:
    responses = model.generate_content("Why is the sky blue?", stream=True)
    for response in responses:
        logger.info(f"response: {response.text}")

    # usage 3:
    prompt = """Create a numbered list of 10 items. Each item in the list should be a trend in the tech industry.

    Each trend should be less than 5 words."""  # try your own prompt

    responses = model.generate_content(prompt, stream=True)

    for response in responses:
        print(response.text, end="")


if __name__ == '__main__':
    typer.run(run)
