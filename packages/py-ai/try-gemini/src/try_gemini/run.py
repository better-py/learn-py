import google.generativeai as genai
import typer
from loguru import logger
from vertexai.language_models import ChatModel, InputOutputTextPair

app = typer.Typer()


@app.command()
def chat(api_key: str):
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


@app.command()
def chat2(temperature: float = 0.2):
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,
        # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    chat = chat_model.start_chat(
        context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
        examples=[
            InputOutputTextPair(
                input_text="How many moons does Mars have?",
                output_text="The planet Mars has two moons, Phobos and Deimos.",
            ),
        ],
    )

    response = chat.send_message(
        "How many planets are there in the solar system?", **parameters
    )
    print(f"Response from Model: {response.text}")

    return response


@app.command()
def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    import vertexai

    # TODO(developer): Update and un-comment below lines
    # project_id = "PROJECT_ID"
    # location = "us-central1"

    vertexai.init(project=project_id, location=location)

    from vertexai.preview.generative_models import GenerativeModel, Part

    multimodal_model = GenerativeModel("gemini-pro-vision")

    response = multimodal_model.generate_content(
        [
            "what is shown in this image?",
            Part.from_uri(
                "gs://generativeai-downloads/images/scones.jpg", mime_type="image/jpeg"
            ),
        ]
    )
    print(response)
    return response.text


if __name__ == '__main__':
    # typer.run(run)
    app()
