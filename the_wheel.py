import openai
import runloop
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam, ChatCompletionAssistantMessageParam, ChatCompletionMessageParam
import json
import pydantic

@runloop.loop
def wheel_it(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    return [f"12345 I am the wheel! let's start simple! {input}"], metadata


@runloop.loop
def sports_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    return [f"The game was close, they had many points"], metadata


_model = "gpt-4-1106-preview"
_client = openai.OpenAI()
_SYSTEM_MSG = ChatCompletionSystemMessageParam(content="You are a degenerate bookie with acute math skills", role="system")


class MessageList(pydantic.BaseModel):
    messages: list[ChatCompletionMessageParam]



@runloop.loop
def open_ai_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    print(metadata)
    user_message = ChatCompletionUserMessageParam(content=input[0], role="user")

    history = json.loads(metadata.get("history", "[]"))

    response = _client.chat.completions.create(
        model=_model,
        messages=[_SYSTEM_MSG] + history + [user_message],
    )
    response.choices[0].message.model_dump_json()

    metadata["history"] = json.dumps(history + [user_message] +
                                     [ChatCompletionAssistantMessageParam(content=response.choices[0].message.content,
                                                                          role="assistant")])

    return [response.choices[0].message.content], metadata
