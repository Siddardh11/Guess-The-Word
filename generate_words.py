import nltk

# Download the words corpus if not already downloaded
nltk.download('words')
from nltk.corpus import words

# Use the NLTK words corpus as a proxy for a standard dictionary.
# Filter: only alphabetic words with a minimum length of 3.
dictionary_words = {
    word.lower() for word in words.words()
    if word.isalpha() and len(word) >= 3
}

# Define a set of technology-related words.
tech_words = {
    "programming", "python", "java", "javascript", "linux", "windows", "macos",
    "operating", "system", "network", "networking", "protocol", "algorithm",
    "database", "server", "client", "firewall", "router", "switch", "cloud",
    "virtualization", "api", "sdk", "compiler", "interpreter", "debugger",
    "code", "software", "hardware", "encryption", "cybersecurity", "machine",
    "learning", "artificial", "intelligence", "blockchain", "cryptocurrency",
    "data", "science", "developer", "programmer", "bit", "byte", "packet",
    "bandwidth", "latency", "throughput", "cache", "kernel", "framework",
    "automation",
    "about", "after", "again", "against", "all", "almost", "also", "always",
    "amazing", "and", "another", "any", "anyone", "anything", "are", "around",
    "as", "ask", "at", "away", "back", "bad", "ball", "band", "bank", "base",
    "be", "beat", "beautiful", "because", "been", "before", "begin", "behind",
    "believe", "best", "better", "between", "big", "bring", "call", "came",
    "can", "care", "carry", "case", "cause", "change", "child", "city", "class",
    "clear", "close", "come", "common", "company", "complete", "continue",
    "cost", "could", "daily", "dance", "dark", "day", "dead", "deal", "death",
    "deep", "describe", "design", "detail", "develop", "different", "direct",
    "do", "doctor", "does", "door", "down", "each", "early", "east", "easy",
    "eat", "effect", "either", "else", "end", "enjoy", "enough", "even",
    "ever", "every", "example", "exist", "expect", "experience", "eye",
    "extra", "face", "fact", "fail", "fall", "family", "far", "fast", "feel",
    "few", "find", "first", "follow", "food", "for", "form", "found", "four",
    "free", "from", "full", "game", "gave", "general", "get", "give", "go",
    "good", "great", "group", "grow", "guess", "guy", "global", "green",
    "ground", "guide", "goal", "gain", "glad", "guard", "had", "half",
    "hand", "happen", "happy", "hard", "have", "head", "hear", "heart",
    "heat", "help", "her", "here", "high", "him", "his", "hold", "home",
    "hope", "idea", "if", "imagine", "important", "in", "include",
    "increase", "indeed", "information", "inside", "interest", "into",
    "is", "it", "item", "iron", "issue", "itself", "image", "invite",
    "job", "join", "just", "joy", "judge", "jump", "joke", "journal",
    "junior", "jazz", "jelly", "jacket", "jewel", "jog", "juice",
    "jungle", "jury", "jeans", "jostle", "jolt", "keep", "key", "kind",
    "king", "know", "knock", "kitchen", "knee", "knife", "knit", "knot",
    "karma", "kangaroo", "kernel", "kitten", "kettle", "keypad", "khaki",
    "kayak", "kept", "lack", "lady", "land", "large", "last", "late",
    "laugh", "lead", "learn", "least", "leave", "left", "life", "light",
    "like", "line", "list", "little", "live", "long", "made", "main",
    "make", "man", "many", "matter", "mean", "measure", "media", "meet",
    "member", "memory", "mind", "minute", "miss", "moment", "money",
    "more", "most", "move", "name", "nation", "nature", "near", "need",
    "never", "new", "next", "night", "no", "not", "note", "nothing",
    "now", "number", "nurse", "normal", "north", "novel", "nobody",
    "object", "observe", "of", "off", "offer", "office", "often",
    "oil", "ok", "old", "on", "once", "one", "only", "open", "or",
    "order", "other", "our", "out", "page", "pair", "paper", "part",
    "pass", "past", "pay", "people", "per", "perhaps", "picture",
    "piece", "place", "plan", "play", "point", "police", "poor",
    "power", "problem", "quality", "quarter", "question", "quick",
    "quiet", "quit", "quote", "quiz", "quaint", "queen", "query",
    "quicken", "quarrel", "quiver", "quench", "quorum", "quilt",
    "quack", "quantum", "quintet", "race", "radio", "rain", "raise",
    "range", "rate", "read", "ready", "real", "reason", "receive",
    "record", "red", "reduce", "refer", "region", "remain",
    "remember", "rest", "right", "safe", "same", "say", "scene",
    "school", "science", "see", "seem", "sell", "send", "sense",
    "serve", "set", "seven", "several", "shall", "shape", "share",
    "she", "show", "table", "take", "talk", "teach", "team", "tell",
    "term", "test", "than", "thank", "that", "the", "their", "them",
    "then", "there", "these", "they", "thing", "think", "under",
    "unit", "united", "unique", "usual", "use", "user", "upper",
    "uncle", "until", "upset", "urban", "utility", "update",
    "urge", "unwind", "unfold", "union", "utilize", "untold",
    "valid", "value", "various", "very", "vessel", "victory",
    "view", "village", "visit", "voice", "volume", "vote",
    "vivid", "vocal", "veteran", "vendor", "visual", "vapor",
    "vulnerable", "vehicle", "wait", "walk", "wall", "want",
    "warm", "was", "watch", "water", "way", "we", "wear", "week",
    "well", "went", "were", "what", "when", "where", "which",
    "while", "xenon", "xylophone", "xylitol", "xenial", "xenophobia",
    "xerosis", "xenophile", "xenograft", "xenolith", "xanthic",
    "xanthous", "xiphoid", "xenogeneic", "xylocarp", "xylotomy",
    "xyster", "xenogenesis", "xenogeny", "xenocryst", "xylograph",
    "yacht", "yard", "year", "yellow", "yes", "yield", "young",
    "youth", "yummy", "yell", "yawn", "yodel", "yonder", "yarn",
    "yoke", "yuppie", "yesterday", "yelp", "yearn", "yolk",
    "zebra", "zero", "zone", "zoo", "zoom", "zeal", "zenith",
    "zephyr", "zest", "zigzag", "zip", "zinc", "zion", "zodiac",
    "zombie", "zoology", "zipper", "zesty", "zany", "zealous"
}

# Filter the technology words to include only alphabetic words with a minimum length of 3.
filtered_tech_words = {
    word.lower() for word in tech_words
    if word.isalpha() and len(word) >= 3
}

# Combine the dictionary words and technology words.
combined_words = dictionary_words.union(filtered_tech_words)

# Write the combined word list to words.txt (one word per line)
with open("words.txt", "w") as f:
    for word in sorted(combined_words):
        f.write(word + "\n")

print("words.txt created with", len(combined_words), "words.")
