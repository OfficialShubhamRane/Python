#  Dictionaries basics
person = {
    "name": "Shubham Rane",
    "contact": "9867717600",
    "email": "shubham16.ranez@gmail.com",
    "birthdate": "Sept 29 1997",
    "isMarried": True
};

print( person.get("birthdate") );
print( person.values() ); # Only Values
print( person.keys() ); # Only keys
print( person.items()); # All key value pairs

# Digits to words conversion
digit_to_words_Dict = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five"
};

digits = input( "Input: " );
word = "";
for digit in digits:
    word += ( digit_to_words_Dict.get(digit, "<!>") + " ") ;

print(word);

# Emoji Mapper
emoji_mapper = {
    ":)": "😊",
    ":(": "☹",
    "B)": "😎",

}
sentence = input("> ");
words = sentence.split(" ");
result = "";
for word in words:
    result += ( emoji_mapper.get(word, word) + " " );
print(result);