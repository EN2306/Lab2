import Lab2

# Test find_min_max()
def test_find_min_max():
    temperatures = [30, 25, 35, 28, 20]
    result = Lab2.find_min_max(temperatures)

    assert result == [20, 35]


# Test calc_average()
def test_calc_average():
    temperatures = [20, 25, 30, 35, 40]
    result = Lab2.calc_average(temperatures)

    assert result == 30


# Test calc_median_temperature() - Odd number of values
def test_calc_median_odd():
    temperatures = [20, 30, 25, 35, 40]
    result = Lab2.calc_median_temperature(temperatures)

    assert result == 30


# Test calc_median_temperature() - Even number of values
def test_calc_median_even():
    temperatures = [20, 30, 25, 35]
    result = Lab2.calc_median_temperature(temperatures)

    assert result == 27.5
