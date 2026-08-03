import os
from openai import OpenAI


def get_ai_response(task: str, code: str) -> str:
    """Send a developer task and code snippet to the OpenAI API."""

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return (
            "Error: OPENAI_API_KEY is missing.\n"
            "Add your API key as an environment variable before running the app."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an AI developer assistant.

Task:
{task}

Code:
{code}

Provide a clear, practical and developer-friendly response.
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt,
        )
        return response.output_text

    except Exception as error:
        return f"API request failed: {error}"


def main() -> None:
    print("=" * 50)
    print("AI Developer Assistant")
    print("=" * 50)

    print("\nChoose a task:")
    print("1. Review code")
    print("2. Explain code")
    print("3. Find possible bugs")
    print("4. Generate documentation")
    print("5. Suggest unit tests")

    choice = input("\nEnter option 1–5: ").strip()

    tasks = {
        "1": "Review this code and suggest improvements.",
        "2": "Explain this code in simple language.",
        "3": "Find possible bugs, security issues and edge cases.",
        "4": "Generate clear documentation for this code.",
        "5": "Suggest useful unit tests for this code.",
    }

    if choice not in tasks:
        print("Invalid option. Please select a number from 1 to 5.")
        return

    print("\nPaste your code below.")
    print("Type END on a new line when finished:\n")

    code_lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        code_lines.append(line)

    code = "\n".join(code_lines)

    if not code.strip():
        print("No code was provided.")
        return

    print("\nGenerating response...\n")
    result = get_ai_response(tasks[choice], code)
    print(result)


if __name__ == "__main__":
    main()
