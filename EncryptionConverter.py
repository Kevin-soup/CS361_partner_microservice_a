# Name: Kevin Lin
# Course: CS361 - Software Engineering I
# Assignment: Microservice A
# Description: This microservice converts messages between binary and plaintext using ZeroMQ.

import zmq
import time

def auto_detection(text: str) -> bool:
    """
    :param text: String sent from main program.
    :return: True if binary. False if plaintext.

    Determines whether input string is plaintext or binary.
    """

    # Separate input text by space. Removes leading or trailing spaces.
    separated_text = text.strip().split()

    # Check if each piece matches with plaintext or binary.
    for piece in separated_text:
        if not set(piece).issubset({"0", "1"}):
            return False

    return True

def plaintext(text: str) -> str:
    """
    :param text: String of plaintext to be converted.
    :return: String of binary values.

    Converts input plaintext string to its binary representation.
    """
    binary_string = ""

    # Format each text character into 8 bit binary.
    for character in text:
        result = format(ord(character), "08b")
        binary_string += result + " "                      # Separate binary characters with spaces.

    return binary_string

def binary(text: str) -> str:
    """
    :param text: String of plaintext to be converted.
    :return: String of plaintext values.

    Converts input binary string to its plaintext representation.
    """
    plaintext_string = ""

    # Format each 8 bit binary into plaintext character.
    for binary_character in text.split():
        result = chr(int(binary_character, 2))
        plaintext_string += result

    return plaintext_string


# Set up ZeroMQ environment with a reply socket.
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Print confirmation message that microservice is running.
print("Microservice A is now listening... \r\n")

# While loop constantly listens for requests from main program.
while True:

    message = socket.recv()
    decoded_message = message.decode()                     # Handles the b-prefix.

    # Print confirmation message upon receiving a request.
    print("Microservice A has CONVERTED a message! \r\n")

    # Detect string format sent by request.
    if auto_detection(decoded_message):
        converted_message = binary(decoded_message)        # Converts binary to plaintext.
    else:
        converted_message = plaintext(decoded_message)     # Converts plaintext to binary.

    # Make the program sleep for 1 second.
    time.sleep(1)

    # Send response back to main program.
    socket.send_string(converted_message)


