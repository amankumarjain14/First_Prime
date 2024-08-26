
# Prime Number Finder

This is a simple Streamlit app that allows users to input a series of integers and identifies the first prime number among them. The app is designed to be user-friendly and is suitable for educational purposes or as a basic utility tool.

## Features

- **Input**: Accepts a user-defined number of integers.
- **Prime Number Identification**: Determines and displays the first prime number in the list of integers provided.
- **User Interface**: Simple and interactive web interface powered by Streamlit.

## Requirements

To run this application, you need to have Python installed along with the following Python packages:

- **Streamlit**: For creating the web interface.

You can install Streamlit using pip:

```bash
pip install streamlit
```

## Installation

1. **Clone the repository** (if applicable) or download the script file `prime_finder.py`.

2. **Navigate to the directory** where the script is located.

3. **Install the required package** using pip:

    ```bash
    pip install streamlit
    ```

## Usage

To run the Streamlit app, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where `prime_finder.py` is located.
3. Run the following command:

    ```bash
    streamlit run prime_finder.py
    ```

4. A new tab will open in your web browser displaying the app interface.

### Interface Overview

- **Number of Integers**: Enter the number of integers you want to check for prime numbers.
- **Enter Each Integer**: Input the integers one by one as prompted.
- **Find First Prime Button**: After entering the integers, click this button to find the first prime number.
- **Result**: The first prime number will be displayed if one is found, otherwise an error message will be shown.

## Example

1. Enter `5` as the number of integers.
2. Input the integers `10`, `15`, `23`, `8`, and `17`.
3. The app will identify `23` as the first prime number and display it.

## Code Explanation

The main script is structured as follows:

1. **Prime Check Function**:
    - A helper function `is_prime` checks if a given number is prime by verifying if it has any divisors other than 1 and itself.

2. **Streamlit Interface**:
    - The user inputs the total number of integers.
    - The user then inputs each integer one by one.
    - On pressing the "Find First Prime" button, the app checks each integer in the order entered to find and display the first prime number.

3. **Output**:
    - If a prime number is found, it's displayed using `st.success()`.
    - If no prime number is found, an error message is displayed using `st.error()`.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or issues, feel free to open an issue or submit a pull request.

## Contact

If you have any questions or need further assistance, please feel free to contact me at [your-email@example.com].
