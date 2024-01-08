def rectangle(length, width):
    
    if type(length) != int or type(width) != int:

        return 'Enter valid values!'
    
    def area(length, width):

        return f"Rectangle area: {length * width}\n"
    
    def perimeter(length, width):

        return f"Rectangle perimeter: {2*(length+width)}"
    
    return area(length, width) + perimeter(length, width)

print(rectangle(2, 10))