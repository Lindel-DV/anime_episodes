# Instructions for creating lists:
# Here is the structure you will use for the 'Search_list':
# Include key pieces of information: ["Title", "Author", "Artist", "Main_Character1", "Main_Character2", "Main_Character3", "Year_Written", "My_Personal_Opinion"]

# Note that you should provide real values for each field when using 'Search_list'.
# Example:
# Search_list = ["Naruto", "Masashi Kishimoto", "Masashi Kishimoto", "Naruto Uzumaki", "Sasuke Uchiha", "Sakura Haruno", 1999, "A nostalgic masterpiece!"]

# To create and add multiple entries, you can use methods such as 'append' or a more complex data structure like a list of dictionaries.

# Example of handling multiple entries:
Anime_Episodes = [
    {
        "Title": "Naruto",
        "Author": "Masashi Kishimoto",
        "Artist": "Masashi Kishimoto",
        "Main_Character1": "Naruto Uzumaki",
        "Main_Character2": "Sasuke Uchiha",
        "Main_Character3": "Sakura Haruno",
        "Year_Written": 1999,
        "My_Personal_Opinion": "A nostalgic masterpiece!"
    },
    {
        "Title": "Attack on Titan",
        "Author": "Hajime Isayama",
        "Artist": "Hajime Isayama",
        "Main_Character1": "Eren Yeager",
        "Main_Character2": "Mikasa Ackerman",
        "Main_Character3": "Armin Arlert",
        "Year_Written": 2009,
        "My_Personal_Opinion": "A thrilling and dark adventure."
    }
]

# Example Usage:
from shared_lists import Anime_Episodes, USER_ROLES, SUPPORTED_COUNTRIES

print("Allowed roles:", USER_ROLES)
if "admin" in USER_ROLES:
    print("Admin access granted.")

