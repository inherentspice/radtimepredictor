from radtimepredictor.radify import rad_time

def test_but_not_really():
    assert type(rad_time(test=True)) == str
