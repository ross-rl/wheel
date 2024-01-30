import runloop


@runloop.loop
def wheel_it(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    return [f"I am the wheel! let's start simple! {input}"], metadata


@runloop.loop
def sports_data(metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
    return [f"The game was close, they had many points"], metadata

