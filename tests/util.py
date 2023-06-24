def get_mock_pipe(
        value,
        expect_topic_input,
        expect_topic_output
):
    def mock_pipe(topic_input, topic_output=None):
        def decorator(func):
            async def wrapper(*args, **kwargs):
                print(topic_input, topic_output)
                assert expect_topic_input == topic_input
                assert expect_topic_output == topic_output
                data = await func(value, *args, **kwargs)
                return data
            return wrapper
        return decorator
    return mock_pipe
