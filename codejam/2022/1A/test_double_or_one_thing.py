import importlib
from io import StringIO


def test_double_or_one_thing(monkeypatch, capsys):
    sample_input = StringIO('3\nPEEL\nAAAAAAAAAA\nCODEJAMDAY')
    monkeypatch.setattr('sys.stdin', sample_input)
    module = importlib.import_module('double_or_one_thing')
    captured = capsys.readouterr()
    assert captured.out == 'Case #1: PEEEEL\nCase #2: AAAAAAAAAA\nCase #3: CCODDEEJAAMDAAY\n'
