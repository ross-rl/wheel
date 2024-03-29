import pydantic
import runloop
import time


class WheelRequest(pydantic.BaseModel):
    echo: str


class WheelResponse(pydantic.BaseModel):
    echo: str


class KvStorageSimple(pydantic.BaseModel):
    k1: str = ""


@runloop.function
def wheel_it(request: WheelRequest) -> WheelResponse:
    return WheelResponse(echo=f"12345 I am the wheel, echo! {request}")


@runloop.function
def concat(request: WheelRequest, s1: runloop.Session[KvStorageSimple]) -> WheelResponse:
    s1.kv.k1 = s1.kv.k1 + " <> " + request.echo
    return WheelResponse(echo=s1.kv.k1)


class KvStorageCounter(pydantic.BaseModel):
    k1: int = 0


import time
@runloop.function
def strm(request: int, s1: runloop.Session[KvStorageCounter]) -> int:
    s1.kv.k1 = request + 1
    s1.commit_session()
    time.sleep(1)
    s1.kv.k1 = s1.kv.k1 + 1
    s1.commit_session()
    time.sleep(1)
    s1.kv.k1 = s1.kv.k1 + 1
    s1.commit_session()
    time.sleep(1)
    s1.kv.k1 = s1.kv.k1 + 1
    s1.commit_session()
    time.sleep(1)
    s1.kv.k1 = s1.kv.k1 + 1
    s1.commit_session()
    time.sleep(1)

    print("Returning!")
    return s1.kv.k1


@runloop.async_function
def scheduled(request: int) -> int:
    print("executed scheduled job!")
    return request


@runloop.function
def schedule(request: int, scheduler: runloop.Scheduler) -> int:
    print("running synchronous schedule job!")
    scheduled_time = int((time.time_ns() + 40 * 1_000_000_000) / 1_000_000)
    print(f"scheduling 40 seconds out at time {scheduled_time} ms")
    scheduler.schedule_at_time(scheduled(request), scheduled_time)
    return 0

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
