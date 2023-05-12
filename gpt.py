import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
message = [ {"role": "system", "content": 
              "You are a text summarizer."},
              {"role": "user",
              "content":"Summarize the given text: ChatGPT is a large language model developed by OpenAI, based on the GPT-3 architecture. This advanced conversational AI has revolutionized the field of natural language processing, offering a powerful tool for a wide range of applications. ChatGPT has a vast knowledge base that allows it to generate human-like responses to text-based queries. Additionally, ChatGPT is capable of completing tasks such as translation, summarization, and sentiment analysis. Its ability to learn from previous conversations and adapt its responses accordingly makes it an extremely powerful tool for a wide range of applications, including customer service, education, and healthcare. ChatGPT has had a significant impact on the field of natural language processing, making it easier for individuals and businesses to communicate with customers, patients, and clients, without the need for a human intermediary. This has led to significant cost savings for businesses and improved access to information for individuals. ChatGPT has also facilitated the development of more advanced chatbots and virtual assistants. Despite its impressive capabilities, ChatGPT still has some limitations, including its tendency to generate biased or offensive responses and its limitation to text-based conversations. However, the potential for ChatGPT and other advanced conversational AI is immense, with future versions expected to address many of the current limitations and integrate with other technologies such as machine learning and computer vision. Advanced conversational AI such as ChatGPT will likely continue to play an important role in the future of natural language processing, improving communication and access to information for individuals and businesses alike." }]
# Generate a response
chat = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=message
)
print(chat['choices'][0]['message']['content'])