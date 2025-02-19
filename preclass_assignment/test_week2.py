"""Test your functions from Week 2 assignment.
"""
import functions as fxn


def test_greet(capsys):
    """Check that the greet function prints as expected"""
    # given
    name = 'world'  # who should we greet?
    # when
    fxn.greet(name)  # greet them
    captured = capsys.readouterr()  # capture what would have been printed to screen
    # then
    assert captured.out == 'Hello, world!\n'  # check that the greeting was what we expect



def test_goldilocks(capsys):
    """Check goldilocks returns expected output"""
    # given
    inp= 139 # bed size
    # when
    fxn.goldilocks(inp)
    captured= capsys.readouterr()

    # then
    assert captured.out== 'The bed was to small, Goldilocks was not happy!!\n '  # ! Update the contents of this function so it correctly tests goldilocks

def test_goldilocks_all(capsys):
    """Check goldilocks returns expected output"""
    # given
    bed_sizes = [139, 140, 151, 150]  # bed sizes
    expected_outputs = [
        'The bed was too big, Goldilocks was not happy!!\n',
        'Goldilocks was happy, and would have extended her gratitude, if she was not sleeping already.\n',
        'The bed was too big, Goldilocks was not happy!!\n',
        'The bed was too big, Goldilocks was not happy!!\n'
    ]

    # when & then
    for size, expected in zip(bed_sizes, expected_outputs):
        fxn.goldilocks(size)  
        captured = capsys.readouterr()
        assert captured.out == expected, f"For bed size {size}, expected '{expected.strip()}' but got '{captured.out.strip()}'"



def test_square_list():
    """Check square_list returns expected output"""
    # given
    inp = [1, 2, 3]  # test input to function
    exp_out = [1, 4, 9]  # expected output
    # when
    out = fxn.square_list(inp)  # actual output
    # then
    assert exp_out == out  # throw error if actual and expected output don't match

# this function compares the expected output with the actual output. If it doesn't match it will display an error message.


def test_fibonacci_stop():
    """Check fibonacci functions works as expected."""
    # given
    inp= [30]#number when the function stops
    exp_outp= [1, 1, 2, 3, 5, 8, 13, 21] # spected output
    #when
    out=fxn.fibonacci_stop(inp)
    # then
    assert exp_outp==out  # TODO! Update the contents of this function so it correctly tests fibonacci_stop


def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    # when
    # then
    assert False  # TODO! Update the contents of this function so it correctly tests clean_pitch



def test_clean_pitch():
    """Check clean_pitch works as expected."""
    # given
    inp_x = [-1, 2, 6, 95]  
    inp_status= [1, 0, 0, 0]

    exp_out = [-999, 2, 6, 95]  
    
    # when
    out = fxn.clean_pitch(inp_x, inp_status)  
    
    # then
    assert exp_out == out  
