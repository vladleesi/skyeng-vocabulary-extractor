from bs4 import BeautifulSoup

# Path to your downloaded HTML file
file_path = 'path/to/your/file.html'  # Replace with your actual HTML file path
output_file_path = 'path/to/output_file.txt'  # Replace with your desired output file path

# Open and read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the text from <vim-word> and <div class="translation"> tags
words = soup.find_all('vim-word')
translations = soup.find_all('div', class_='translation')

# Use a set to avoid duplicates
unique_entries = set()

# Iterate through the words and corresponding translations
for word, translation in zip(words, translations):
    word_text = word.get_text(strip=True)
    translation_text = translation.get_text(strip=True)
    
    # Add the pair to the set (set will handle duplicates)
    unique_entries.add(f"{word_text};{translation_text}")

# Sort the entries alphabetically
sorted_entries = sorted(unique_entries)

# Count the number of unique entries
unique_word_count = len(sorted_entries)

# Write the sorted and unique entries to the output file with the count at the top
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Write the count of unique words as the first line
    output_file.write(f"Unique word count: {unique_word_count}\n")
    
    # Write each sorted and unique entry to the file
    for entry in sorted_entries:
        output_file.write(f"{entry}\n")

print(f"Tag values extracted, duplicates removed, sorted alphabetically, and saved to {output_file_path}")
