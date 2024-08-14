import streamlit as st
from groq import Groq

client = Groq(api_key='Your_API_Key')

st.title('Streamlit Chat App')
st.subheader('Welcome to the chat app!')
st.write('Please enter your message below and click on the "Send" button to get a response from the chatbot.')

def main():
    message = st.text_input('Enter your message here:')

    if st.button('Send'):
        st.write('You: ' + message)
        chat_completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
        )

        if chat_completion.choices:
            st.write('Bot: ' + chat_completion.choices[0].message.content)
        else:
            st.write('Bot: No response found')

if __name__ == '__main__':
    main()
