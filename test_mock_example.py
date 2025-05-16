from app import get_user_age

def test_get_user_age(mocker):
  mock_db = mocker.patch('app.database.fetch_user')
  mock_db.return_value = {'name': 'John', 'age': 30}

  assert get_user_age(1) == 30
