def filter_odd(numbers):
    """
    Fungsi untuk menyaring angka ganjil dari list angka.
    """
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

# Contoh penggunaan
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Angka ganjil dari list:", filter_odd(sample_list))
