
import openai

# Replace with your OpenAI API Key
openai.api_key = 'your_openai_api_key_here'

faq_data = [
    {"question": "How can I track my order?", "answer": "You can track your order in the 'My Orders' section."},
    {"question": "What is your return policy?", "answer": "Returns are accepted within 10 days of delivery."},
    {"question": "How do I cancel my order?", "answer": "Go to 'My Orders' and select the item to cancel."},
    {"question": "Do you offer international shipping?", "answer": "Yes, international shipping is available."},
    {"question": "How can I contact customer support?", "answer": "Contact us via chat or call 1800-123-456."}
]

def build_prompt(user_question):
    faqs = "\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in faq_data])
    return (
        f"Below are some frequently asked questions and answers:\n\n"
        f"{faqs}\n\n"
        f"User: {user_question}\n"
        f"Answer:"
    )

def ask_bot():
    print("Welcome to the E-Commerce FAQ Chatbot!\nType 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        prompt = build_prompt(user_input)

        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.4
            )
            answer = response.choices[0].text.strip()

            if "Sorry" in answer or answer == "":
                print("Bot: Sorry, I can only answer questions related to our store policies.")
            else:
                print("Bot:", answer)
        except Exception as e:
            print("Bot: Something went wrong. Check your API key or connection.")
            print("Error:", e)

if __name__ == "__main__":
    ask_bot()
