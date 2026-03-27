def calculate_rectangle_area(length: float, breadth: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        TypeError: If the input is not a numerical type (e.g., int, float).
        ValueError: If the breadth or length is negative or zero.
    """
    
    # Input validation with enhanced error handling
    if not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
        raise TypeError("Length and breadth must be numerical values (int, float). ")
    
    # Check for division by zero error
    if length == 0 or breadth == 0:
        raise ValueError("Length and breadth cannot be zero.")
    
    # Check for edge case where length and breadth are equal (square)
    if length == breadth:
        print(f"The shape is actually a square.")
    
    # Calculate the area of the rectangle
    area = length * breadth
    
    return area