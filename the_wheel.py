import pydantic
import runloop


class WheelRequest(pydantic.BaseModel):
    echo: str


class WheelResponse(pydantic.BaseModel):
    echo: str


@runloop.function
def wheel_it(request: WheelRequest) -> WheelResponse:
    return WheelResponse(echo=f"12345 I am the wheel, echo! {request}")


#
# @runloop.loop
# def sports_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
#     return [f"The game was close, they had many points"], metadata
#
#
# from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam, ChatCompletionAssistantMessageParam, ChatCompletionMessageParam
#
# _model = "gpt-4-1106-preview"
# _client = openai.OpenAI()
# _SYSTEM_MSG = ChatCompletionSystemMessageParam(content="You are a degenerate bookie with acute math skills", role="system")
#
# @runloop.loop
# def open_ai_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
#     print(metadata)
#     user_message = ChatCompletionUserMessageParam(content=input[0], role="user")
#
#     history = json.loads(metadata.get("history", "[]"))
#
#     response = _client.chat.completions.create(
#         model=_model,
#         messages=[_SYSTEM_MSG] + history + [user_message],
#     )
#     response.choices[0].message.model_dump_json()
#
#     metadata["history"] = json.dumps(history + [user_message] +
#                                      [ChatCompletionAssistantMessageParam(content=response.choices[0].message.content,
#                                                                           role="assistant")])
#
#     return [response.choices[0].message.content], metadata
#
# _HISTORY_KEY = "history"
#
#
# @runloop.loop
# def ex_chat(
#     metadata: dict[str, str],
#     inputs: list[str]
# ) -> tuple[list[str], dict[str, str]]:
#     print(f"handle_input metadata={metadata} input={inputs}")
#     next_user_line = {"role": "user", "content": inputs[0]}
#     existing_non_system_messages = json.loads(metadata.get(_HISTORY_KEY, "[]"))
#
#     messages_to_process = existing_non_system_messages + [next_user_line]
#     response = _client.chat.completions.create(
#         model=_model,
#         messages=[_SYSTEM_MSG] + messages_to_process,
#     )
#
#     print(f"got response={response}")
#     # TODO: determine how to propagate errors
#     ai_response_message = response.choices[0].message
#
#     metadata[_HISTORY_KEY] = json.dumps(
#         messages_to_process + [ai_response_message])
#
#     return [ai_response_message.content], metadata
