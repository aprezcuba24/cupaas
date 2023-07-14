import pytest
from unittest.mock import MagicMock, Mock
from app.functions import github_events


repoitory_url = "url_repository"
repoitory_ref = "project_ref"
repoitory_after = "repoitory_after"
data = {
    "body": {
        "ref": repoitory_ref,
        "after": repoitory_after,
        "repository": {
            "full_name": "project_full_name",
            "url": repoitory_url,
        }
    }
}


def get_mock_mongo(project):
    mongo = MagicMock()
    collection = MagicMock()
    find_one = Mock(return_value=project)
    insert_one = Mock()
    collection.find_one = find_one
    collection.insert_one = insert_one
    mongo.get_collection = Mock(return_value=collection)
    return mongo, find_one, insert_one


@pytest.mark.asyncio
async def test_github_events_project_not_foud():
    mock_mongo, mock_find_one, _ = get_mock_mongo(None)
    result = await github_events(data, context={
        "mongo": mock_mongo,
    })
    assert result is None
    mock_find_one.assert_called_once_with({
        "name": "project_full_name",
        "git_source": "github",
        "ref": "project_ref",
    })


@pytest.mark.asyncio
async def test_github_events_project_foud():
    project = {
        "_id": "project_id",
    }
    mock_mongo, mock_find_one, mock_insert_one = get_mock_mongo(project)
    result = await github_events(data, context={
        "mongo": mock_mongo,
    })
    zip_url = f"{repoitory_url}/archive/{repoitory_ref}.zip"
    assert result == {
        "project": project,
        "zip_url": zip_url,
        "commit_hash": repoitory_after,
    }
    mock_find_one.assert_called_once_with({
        "name": "project_full_name",
        "git_source": "github",
        "ref": "project_ref",
    })
    mock_insert_one.assert_called_once_with({
        "project_id": "project_id",
        "data": data,
    })
