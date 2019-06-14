# Import Necessary Libaries
import dill
import pickle
from textblob import TextBlob

# Load the model from disk
spamDetector = pickle.load(open('model.sav', 'rb'))

# Load trainingVector function from disk
dill_file = open("trainingVector", "rb")
trainingVector = dill.load(dill_file)

# Split into words


def SplitIntoWords(message): return TextBlob(message.lower()).words


# Classify user input to spam or ham
userInp = input("Enter your message\n")
print("\nOh!, thats a ", spamDetector.predict(
    trainingVector.transform([userInp]))[0])
