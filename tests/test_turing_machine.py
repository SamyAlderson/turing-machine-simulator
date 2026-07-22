import pytest
from turing_machine import TuringMachine

def test_turing_machine_init():
    tm = TuringMachine()
    assert tm.tape == {}

def test_turing_machine_write():
    tm = TuringMachine()
    tm.write('A', 0)
    assert tm.tape == {0: 'A'}
    with pytest.raises(ValueError):
        tm.write('A', -1)

def test_turing_machine_read():
    tm = TuringMachine()
    tm.write('A', 0)
    assert tm.read(0) == 'A'
    with pytest.raises(KeyError):
        tm.read(-1)

def test_turing_machine_move_left():
    tm = TuringMachine()
    tm.write('A', 0)
    tm.move_left()
    assert tm.tape == {0: 'A', -1: None}
    with pytest.raises(ValueError):
        tm.move_left()

def test_turing_machine_move_right():
    tm = TuringMachine()
    tm.write('A', 0)
    tm.move_right()
    assert tm.tape == {0: 'A', 1: None}
    with pytest.raises(ValueError):
        tm.move_right()

def test_turing_machine_step():
    tm = TuringMachine()
    tm.write('A', 0)
    tm.write('B', 1)
    tm.step()
    assert tm.tape == {0: 'A', 1: 'B'}
    with pytest.raises(ValueError):
        tm.step()

def test_turing_machine_step_with_moves():
    tm = TuringMachine()
    tm.write('A', 0)
    tm.write('B', 1)
    tm.move_left()
    tm.step()
    assert tm.tape == {0: 'A', -1: None, 1: 'B'}
    with pytest.raises(ValueError):
        tm.step()

def test_turing_machine_run():
    tm = TuringMachine()
    tm.write('A', 0)
    tm.write('B', 1)
    tm.run(10)
    assert tm.tape == {0: 'A', 1: 'B'}
    with pytest.raises(ValueError):
        tm.run(-1)