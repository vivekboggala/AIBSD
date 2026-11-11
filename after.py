
def calculate_average(marks):
    """Calculate the average of valid marks."""

    if not marks:
        raise ValueError("At least one mark is required.")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")

    return sum(marks) / len(marks)


def main():
    """Get input, validate marks, and display average."""

    user_input = input(
        "Enter marks separated by spaces: "
    ).strip()

    if not user_input:
        print("Error: Please enter at least one mark.")
        return

    try:
        marks = [float(value) for value in user_input.split()]

        average = calculate_average(marks)

        print(f"Average marks: {average:.2f}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
