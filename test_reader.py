import sys
from XCaliburMethodReader import main

testfile = 'data/test.meth'

def test_parser_accepts_file(capsys):
    args = (testfile,)
    main(args)
    captured = capsys.readouterr()
    assert 'Proxeon' in captured.out
    assert 'Thermo Exactive' in captured.out


def test_thermo_data_text(capsys):
    args = testfile, '-s', 'Thermo Exactive'
    main(args)
    captured = capsys.readouterr()
    assert 'Method' in captured.out

    args = testfile, '-s', 'Thermo Exactive', '--to', 'text'
    main(args)
    captured = capsys.readouterr()
    assert 'Method' in captured.out


def test_thermo_data_json(capsys):
    args = testfile, '-s', 'Thermo Exactive', '--to', 'json'
    main(args)
    captured = capsys.readouterr()
    assert captured.out[0] == '{'
    assert captured.out.strip()[-1] == '}'


def test_thermo_data_xml(capsys):
    args = testfile, '-s', 'Thermo Exactive', '--to', 'xml'
    main(args)
    captured = capsys.readouterr()
    assert captured.out[:5] == '<?xml'
    assert captured.out.strip()[-1] == '>'


def test_ms_data_text(capsys):
    args = testfile, '-s', 'Proxeon_EASY-nLC'
    main(args)
    captured = capsys.readouterr()
    assert 'Sample' in captured.out

    args = testfile, '-s', 'Proxeon_EASY-nLC', '--to', 'text'
    main(args)
    captured = capsys.readouterr()
    assert 'Sample' in captured.out


def test_ms_data_json(capsys):
    args = testfile, '-s', 'Proxeon_EASY-nLC', '--to', 'json'
    main(args)
    captured = capsys.readouterr()
    assert captured.out[0] == '{'
    assert captured.out.strip()[-1] == '}'


def test_ms_data_xml(capsys):
    args = testfile, '-s', 'Proxeon_EASY-nLC', '--to', 'xml'
    main(args)
    captured = capsys.readouterr()
    assert captured.out[:5] == '<?xml'
    assert captured.out.strip()[-1] == '>'


