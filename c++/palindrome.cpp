#include <iostream>

void reverseString(std::string* stringToReverse)
{
    // allocate memory for a new string using the existing string.
    std::string stringCopy(*stringToReverse);
    int stringLength = stringToReverse->length();

    for(int i = 0; i < stringLength - 1; i++)
    {
        std::cout << i << std::endl;
        stringToReverse[i] = stringCopy[stringLength -1 -i];
    }

    return;
}

int main(int argc, char* argv[])
{
    std::string myString = "Hello, World!";
    reverseString(&myString);

    std::cout << myString << std::endl;

    return EXIT_SUCCESS;
}