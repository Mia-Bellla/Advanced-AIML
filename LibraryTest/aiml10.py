import wikipedia

# Ask user for a topic
topic = input("Enter a topic to search on Wikipedia: ")

# Fetch summary
try:
    summary = wikipedia.summary(topic, sentences=3)  # first 3 sentences
    print("\n Wikipedia Summary:")
    print(summary)

    # Optional: get page details
    page = wikipedia.page(topic)
    print("\n Page URL:", page.url)

except wikipedia.exceptions.DisambiguationError as e:
    print("\n That term is too broad! Did you mean one of these?")
    print(e.options[:5])  # show first 5 options

except wikipedia.exceptions.PageError:
    print("\n No page found for that topic.")
