import pytest
from unittest.mock import patch
from tests.util import get_mock_pipe


@pytest.mark.asyncio
async def test_download_code():
    data = {
        "commit_hash": "commit_hash",
        "zip_url": "zip_url",
    }
    with patch("app.kafka.pipe", get_mock_pipe()), patch(
        "app.functions.download_code.download_url"
    ) as mock_download_url, patch(
        "app.functions.download_code.ZipFile"
    ) as mock_extractall, patch(
        "app.functions.download_code.shutil.move"
    ) as mock_move, patch(
        "app.functions.download_code.os.listdir", return_value=["directory"]
    ) as mock_listdir, patch(
        "app.functions.download_code.os.remove"
    ) as mock_remove, patch(
        "app.functions.download_code.os.rmdir"
    ) as mock_rmdir:
        # I need to import the function here to be able to mock the pipe.
        from app.functions import download_code
        result = await download_code(data)
        print(result)
        assert result == {
            'commit_hash': 'commit_hash',
            'zip_url': 'zip_url',
            'project_code': 'DATA/commit_hash'
        }
        mock_download_url.assert_called_once_with(
            "zip_url",
            "DATA/commit_hash_downoload.zip"
        )
        mock_extractall.assert_called_once_with(
            "DATA/commit_hash_downoload.zip",
            "r"
        )
        mock_move.assert_called_once_with(
            'DATA/commit_hash_downoload/directory',
            'DATA/commit_hash'
        )
        mock_listdir.assert_called_once_with("DATA/commit_hash_downoload")
        mock_remove.assert_called_once_with("DATA/commit_hash_downoload.zip")
        mock_rmdir.assert_called_once_with("DATA/commit_hash_downoload")
