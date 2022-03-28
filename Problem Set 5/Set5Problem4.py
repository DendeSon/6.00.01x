# Problem 4 - Decrypt a Story
#
def decrypt_story():
    garb = CiphertextMessage(get_story_string())
    return garb.decrypt_message()