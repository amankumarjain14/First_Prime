import streamlit as st


# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Streamlit App
st.title("Find the First Prime Number")

# Input number of integers
n = st.number_input("Enter the number of integers:", min_value=1, step=1, value=1)

# List to hold integers
integers = []

# Input the integers
for i in range(n):
    integers.append(st.number_input(f"Enter integer {i + 1}:", step=1))

# Button to find the first prime number
if st.button("Find First Prime"):
    prime_number = None
    for number in integers:
        if is_prime(number):
            prime_number = number
            break

    if prime_number:
        st.success(f"The first prime number is: {prime_number}")
    else:
        st.error("No prime numbers found.")
