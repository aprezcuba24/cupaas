from app.config import (
    KAFKA_TOPIC_GITHUB_EVENT,
    KAFKA_TOPIC_DOWNLOAD_CODE,
    KAFKA_TOPIC_VALIDATE_CONFIGURATION
)


pipes = {
    "github_events": (KAFKA_TOPIC_GITHUB_EVENT, KAFKA_TOPIC_DOWNLOAD_CODE),
    "download_code": (
        KAFKA_TOPIC_DOWNLOAD_CODE,
        KAFKA_TOPIC_VALIDATE_CONFIGURATION
    ),
}


def get_mock_pipe():
    def mock_pipe(topic_input, topic_output=None):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                expect_topic_input, expect_topic_output = pipes[func.__name__]
                print(topic_input, topic_output)
                assert expect_topic_input == topic_input, \
                    f"{expect_topic_input}, {topic_input}"
                assert expect_topic_output == topic_output, \
                    f"{expect_topic_output}, {topic_output}"
                data = await func(*args, **kwargs)
                return data
            return wrapper
        return decorator
    return mock_pipe
