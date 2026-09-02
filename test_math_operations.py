"""Tests for mathematical operations."""

import pytest
from math_operations import add, subtract, multiply, divide, power, modulo


class TestAddition:
    """Test cases for addition."""
    
    def test_add_positive_numbers(self):
        print("Running test_add_positive_numbers")
        assert add(2, 3) == 5
        
    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
        
    def test_add_mixed_numbers(self):
        assert add(-5, 10) == 5
        
    def test_add_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5


class TestSubtraction:
    """Test cases for subtraction."""
    
    def test_subtract_positive_numbers(self):
        assert subtract(10, 3) == 7
        
    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2
        
    def test_subtract_mixed_numbers(self):
        assert subtract(5, 10) == -5
        
    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiplication:
    """Test cases for multiplication."""
    
    def test_multiply_positive_numbers(self):
        assert multiply(4, 5) == 20
        
    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12
        
    def test_multiply_mixed_numbers(self):
        assert multiply(-5, 6) == -30
        
    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        
    def test_multiply_by_one(self):
        assert multiply(7, 1) == 7


class TestDivision:
    """Test cases for division."""
    
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        
    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5
        
    def test_divide_mixed_numbers(self):
        assert divide(-10, 2) == -5
        
    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
            
    def test_divide_decimal_result(self):
        assert divide(7, 2) == 3.5


class TestPower:
    """Test cases for power operation."""
    
    def test_power_positive_exponent(self):
        assert power(2, 3) == 8
        
    def test_power_zero_exponent(self):
        assert power(5, 0) == 1
        
    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25
        
    def test_power_of_zero(self):
        assert power(0, 5) == 0


class TestModulo:
    """Test cases for modulo operation."""
    
    def test_modulo_positive_numbers(self):
        assert modulo(10, 3) == 1
        
    def test_modulo_exact_division(self):
        assert modulo(10, 5) == 0
        
    def test_modulo_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot perform modulo with zero"):
            modulo(5, 0)
            
    def test_modulo_negative_numbers(self):
        assert modulo(-10, 3) == 2
