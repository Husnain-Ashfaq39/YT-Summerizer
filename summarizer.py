import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

def summarize_text(text):
    """Summarize the given text using OpenAI's GPT model via LangChain."""
    try:
        # Initialize the OpenAI LLM with the API key
        llm = OpenAI(
            openai_api_key=openai_api_key,
            model_name="gpt-3.5-turbo",  # You can switch to "gpt-4" if available
            temperature=0.5,             # Controls creativity
            max_tokens=150                # Adjust based on desired summary length
        )

        # Define a prompt template for summarization
        prompt = PromptTemplate(
            input_variables=["text"],
            template="Please provide a concise summary of the following text:\n\n{text}"
        )

        # Create a chain with the prompt and LLM
        chain = LLMChain(llm=llm, prompt=prompt)

        # Generate the summary
        summary = chain.run(text)

        return summary.strip()

    except Exception as e:
        return f"An error occurred during summarization: {str(e)}"

# Example usage
if __name__ == "__main__":
    sample_text = """
    OpenAI has developed a new language model that surpasses previous versions in both accuracy and efficiency.
    The model leverages advanced machine learning techniques to understand and generate human-like text,
    making it useful for a wide range of applications, including content creation, customer support, and more.
    """

    summary = summarize_text(sample_text)
    print("Summary:")
    print(summary)
