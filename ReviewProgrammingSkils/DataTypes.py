import math

def volumeSphere(radius: float):
    return (4/3) * math.pi * (radius ** 3)


def storeWholeCopeies(number_of_books):
    book_price = 24.95
    discount = 0.4
    book_wholesale_price = book_price * discount
    
    shipping_first = 3.0
    shipping_additional = 0.75

    if (number_of_books <= 0):
        return 0.0;
    elif (number_of_books == 1):
        return book_wholesale_price + shipping_first
    else:
        return (book_wholesale_price * number_of_books) + shipping_first + (shipping_additional * (number_of_books - 1))

print(volumeSphere(5.0))
print(f'{storeWholeCopeies(60):<1.2f}')