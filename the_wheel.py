import runloop
import openai


@runloop.loop
def wheel_it(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    return [f"I am the wheel! let's start simple! {input}"], metadata


@runloop.loop
def sports_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    return [f"The game was close, they had many points"], metadata


_model = "gpt-4-1106-preview"
_client = openai.OpenAI()
_SYSTEM_MSG = {"role": "system",
               "content": "You are a degenerate bookie"}


@runloop.loop
def open_ai_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    user_message = {"role": "user", "content": f"{input[0]}"}

    response = _client.chat.completions.create(
        model=_model,
        messages=[_SYSTEM_MSG] + [user_message],
    )

    return [response.choices[0].message.content], metadata
