def greet(firstName, lastName):
    print(f"Hello {firstName} {lastName}");

# greet(lastName="Rane", firstName="Shubham");

def square(number):
    return number * number;

print(square(3));

# Takes sentence as a input
# Returns output with emojis in the sentence
def emojiConverter(sentence):
    sentence = str(sentence);
    emojis = {
        ":)": "😀",
        ":(": "☹",
        "B)": "😎",
    };
    result = "";
    words = sentence.split(" ");
    for word in words:
        result += emojis.get(word,word) + " ";

    return result;

print(emojiConverter("Hi Shubham :)"))