import json
from pathlib import Path

import pytest

# читаем тест-данные из JSON (лежат отдельно от кода теста)
DATA_FILE = Path(__file__).parent.parent / "data" / "users.json"
USER_CASES = json.loads(DATA_FILE.read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", USER_CASES, ids=[c["username"] for c in USER_CASES])
def test_user_username_matches_data(api, case):
    resp = api.get(f"/users/{case['id']}")

    assert resp.status_code == 200
    assert resp.json()["username"] == case["username"]
