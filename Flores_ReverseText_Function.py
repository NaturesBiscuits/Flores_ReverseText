def reverse_text():
    while True:
        text = input("Enter a text: ")

        if text.isalpha() or ' ' in text and not any(char.isdigit() for char in text):
            reversed_text = text[::-1]
            print("Reversed text:", reversed_text)
            break
        else:
            print("Error: Please enter text only, no numbers or special characters allowed.")

reverse_text()
