from typing import List
import re
from .base_cleaner import BaseCleaner

class TagsCleaner(BaseCleaner):
    """
    Box: Tags cleaner

    Input: raw tags text
    Output: cleaned tags text
    Responsibility: Clean and format tags
    """

    def __init__(self):
        self.conversational_starts = [
            "here's a", "this is", "let's look", "as an ai", "i can help", "i've extracted",
            "below is", "okay, here's", "the type is", "i would classify this as", "it is a",
            "here's a list", "the following are", "below is the", "here are the"
        ]
        self.stop_words = {
            'to', 'it', 'some', 'and', 'the', 'a', 'in', 'of', 'for', 'on', 'with', 'is', 'that', 'this', 'at', 'by', 'from', 'an', 
            'or', 'as', 'but', 'not', 'your', 'my', 'we', 'you', 'i', 'he', 'she', 'they', 'them', 'us', 'our', 'their', 'which', 
            'who', 'what', 'where', 'when', 'why', 'how', 'each', 'just', 'only', 'all', 'any', 'such', 'so', 'up', 'down', 'out', 
            'off', 'then', 'there', 'here', 'now', 'will', 'would', 'could', 'should', 'can', 'may', 'might', 'must', 'has', 'have', 
            'had', 'do', 'does', 'did', 'was', 'were', 'be', 'been', 'being', 'get', 'got', 'go', 'goes', 'went', 'going', 'say', 
            'says', 'said', 'make', 'makes', 'made', 'making', 'know', 'knows', 'knew', 'knowing', 'see', 'sees', 'saw', 'seeing', 
            'take', 'takes', 'took', 'taking', 'come', 'comes', 'came', 'coming', 'want', 'wants', 'wanted', 'wanting', 'look', 
            'looks', 'looked', 'looking', 'find', 'finds', 'found', 'finding', 'give', 'gives', 'gave', 'giving', 'tell', 'tells', 
            'told', 'telling', 'work', 'works', 'worked', 'working', 'call', 'calls', 'called', 'calling', 'try', 'tries', 'tried', 
            'trying', 'ask', 'asks', 'asked', 'asking', 'need', 'needs', 'needed', 'needing', 'feel', 'feels', 'felt', 'feeling', 
            'become', 'becomes', 'became', 'becoming', 'leave', 'leaves', 'left', 'leaving', 'put', 'puts', 'put', 'putting', 
            'mean', 'means', 'meant', 'meaning', 'keep', 'keeps', 'kept', 'keeping', 'begin', 'begins', 'began', 'beginning', 
            'seem', 'seems', 'seemed', 'seeming', 'help', 'helps', 'helped', 'helping', 'talk', 'talks', 'talked', 'talking', 
            'turn', 'turns', 'turned', 'turning', 'start', 'starts', 'started', 'starting', 'show', 'shows', 'showed', 'showing', 
            'hear', 'hears', 'heard', 'hearing', 'play', 'plays', 'played', 'playing', 'run', 'runs', 'ran', 'running', 'move', 
            'moves', 'moved', 'moving', 'like', 'likes', 'liked', 'liking', 'live', 'lives', 'lived', 'living', 'believe', 
            'believes', 'believed', 'believing', 'hold', 'holds', 'held', 'holding', 'bring', 'brings', 'brought', 'bringing'
        }

    def clean(self, text: str) -> str:
        """Ensures tags are correctly formatted and cleaned."""
        cleaned_text = text.strip().lower()

        # Remove conversational starts
        for phrase in self.conversational_starts:
            if cleaned_text.startswith(phrase):
                cleaned_text = cleaned_text[len(phrase):].strip()

        # Remove punctuation but keep spaces for splitting
        cleaned_text = re.sub(r'[^\w\s#\-]', '', cleaned_text) # Keep alphanumeric, #, -, and spaces

        # Split by whitespace and commas, filter out empty strings
        potential_tags = [tag.strip() for tag in re.split(r'[\s,]+', cleaned_text) if tag.strip()]
        
        cleaned_tags = []
        for tag_word in potential_tags:
            # Ensure it starts with #
            if not tag_word.startswith('#'):
                tag_word = '#' + tag_word

            # Remove invalid characters from within the tag_word itself after the initial #
            tag_word = '#' + re.sub(r'[^\w\-]', '', tag_word[1:])
            
            # Filter out stop words (after removing # for comparison)
            if tag_word[1:] and tag_word[1:] not in self.stop_words:
                cleaned_tags.append(tag_word)
                
        # Remove duplicates and enforce 20 tag limit
        unique_tags = sorted(list(set(cleaned_tags)))
        return " ".join(unique_tags[:20])
