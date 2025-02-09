import difflib
from googletrans import Translator

def read_text_from_file(file_path):
    """Reads text from a given file path and returns it as a string."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading '{file_path}': {e}")
        return None

def write_text_to_file(file_path, content):
    """Writes the given text content to a file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to '{file_path}': {e}")

def extract_first_n_words(text, n=100):
    """Extracts the first n words from the provided text."""
    words = text.split()
    return " ".join(words[:n])

def translate_to_french(text):
    """Translates text from English to French using googletrans."""
    translator = Translator()
    try:
        result = translator.translate(text, dest='fr')
        return result.text
    except Exception as e:
        print("An error occurred while translating to French:", e)
        return None

def translate_back_to_english(text):
    """
    Translates text from French back to English.
    Currently uses googletrans, but can be replaced with MyMemoryTranslator.
    """
    translator = Translator()
    try:
        result = translator.translate(text, dest='en')
        return result.text
    except Exception as e:
        print("An error occurred while translating back to English:", e)
        return None

def compute_unified_diff(original_text, modified_text):
    """
    Computes the unified diff between two text strings and returns a list of diff lines.
    """
    original_words = original_text.split()
    modified_words = modified_text.split()
    diff_lines = difflib.unified_diff(
        original_words, 
        modified_words, 
        fromfile='original', 
        tofile='translated', 
        lineterm=''
    )
    return list(diff_lines)

def main():
    # 1. Read the sample text
    sample_text = read_text_from_file("sample_text.txt")
    if sample_text is None:
        return  # Exit if there was an error reading the file
    
    # 2. Extract the first 100 words
    original_text = extract_first_n_words(sample_text, 100)
    
    # 3. Translate the text to French
    translated_text_in_french = translate_to_french(original_text)
    if translated_text_in_french is None:
        return  # Exit if there was an error during French translation
    
    print("Text translated to French:")
    print(translated_text_in_french, "\n")
    
    # 4. Translate back from French to English
    translated_back_to_english = translate_back_to_english(translated_text_in_french)
    if translated_back_to_english is None:
        return  # Exit if there was an error during back translation
    
    print("Text translated back to English:")
    print(translated_back_to_english, "\n")
    
    # 5. Compute the unified diff
    diff_result = compute_unified_diff(original_text, translated_back_to_english)
    
    # 6. Write the differences to a file
    diff_filename = "translation_diff.txt"
    diff_content = "\n".join(diff_result)
    write_text_to_file(diff_filename, diff_content)
    print(f"Differences have been written to '{diff_filename}'.")

if __name__ == "__main__":
    main()
