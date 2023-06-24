import pytest
from unittest.mock import patch, MagicMock, Mock
from app.webhook import github_webhook
from app.config import KAFKA_TOPIC_GITHUB_EVENT


@patch("app.webhook.send_message")
@pytest.mark.asyncio
async def test_github_webhook(mock_send_message):
    request = MagicMock()
    data = {
        "body": {"a": 1},
        "headers": {"b": 2}
    }

    async def json():
        return data["body"]
    request.json = json
    request.headers.items = Mock(return_value=[("b", 2)])
    await github_webhook(request)
    mock_send_message.assert_called_once_with(
        KAFKA_TOPIC_GITHUB_EVENT,
        data
    )
