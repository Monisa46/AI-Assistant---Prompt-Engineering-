import streamlit as st
from summa import summarizer
import wikipedia
import random

# ----------------------------
# Title
# ----------------------------
st.set_page_config(page_title="AI Assistant", layout="centered")
st.title("🤖 AI Assistant - Prompt Engineering Project")

# ----------------------------
# Sidebar - Function Selection
# ----------------------------
task = st.sidebar.selectbox("Choose a Function", [
    "Summarize Text",
    "Answer a Question",
    "Generate a Story"
])

# ----------------------------
# Function: Summarization
# ----------------------------
if task == "Summarize Text":
    st.subheader("📄 Summarize Text")
    user_text = st.text_area("Enter a paragraph:")
    if st.button("Summarize"):
        if user_text:
            summary = summarizer.summarize(user_text, ratio=0.5)
            if summary:
                st.success("Summary:")
                st.write(summary)
            else:
                st.warning("Try entering a longer or clearer paragraph.")
        else:
            st.error("Please enter text to summarize.")

# ----------------------------
# Function: Wikipedia Q&A
# ----------------------------
elif task == "Answer a Question":
    st.subheader("❓ Answer a Factual Question")
    user_question = st.text_input("Ask something:")
    if st.button("Get Answer"):
        try:
            answer = wikipedia.summary(user_question, sentences=2)
            st.success("Answer:")
            st.write(answer)
        except wikipedia.exceptions.DisambiguationError as e:
            st.warning(f"Too broad. Try one of: {e.options[:5]}")
        except wikipedia.exceptions.PageError:
            st.error("No matching Wikipedia page found.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# ----------------------------
# Function: Story Generator
# ----------------------------
elif task == "Generate a Story":
    st.subheader("📝 Generate a Story")
    theme = st.text_input("Enter a theme (e.g., magic, treasure, robot):")
    if st.button("Generate Story"):
        if theme:
            phrases = [
                f"Once upon a time in a world of {theme}",
                f"a curious traveler discovered a {theme}",
                f"hidden within the shadows of the mountains",
                f"was a secret {theme}",
                f"that changed everything",
                f"they followed clues etched in old scrolls",
                f"facing dangers and wonders alike",
                f"until they reached the heart of the {theme}",
                f"where a choice awaited them",
                f"and the fate of the land was sealed"
            ]
            story = " ".join(random.choices(phrases, k=5)) + "."
            st.success("Here’s your story:")
            st.write(story)
        else:
            st.error("Please enter a theme to generate a story.")
