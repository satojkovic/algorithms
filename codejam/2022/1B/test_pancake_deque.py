import importlib
import pytest
import os
from io import StringIO


@pytest.fixture
def input_data():
    inputs = {}
    with open(os.path.join('test_data', 'sample_test_set_1', 'sample_ts1_input.txt')) as f:
        inputs['sample_ts1_input'] = ''.join(f.readlines())
    return inputs


@pytest.fixture
def output_data():
    outputs = {}
    with open(os.path.join('test_data', 'sample_test_set_1', 'sample_ts1_output.txt')) as f:
        outputs['sample_ts1_output'] = ''.join(f.readlines())
    return outputs


def test_pancake_deque(monkeypatch, capsys, input_data, output_data):
    sample_input = StringIO(input_data['sample_ts1_input'])
    monkeypatch.setattr('sys.stdin', sample_input)
    module = importlib.import_module('pancake_deque')
    captured = capsys.readouterr()
    assert captured.out == output_data['sample_ts1_output']
