from ollama import chat

while True:

    user = input("You: ")

    if user=="exit":
        break

    response = chat(

        model="llama3.2",

        messages=[

        {"role":"user","content":user}

        ]

    )

    print(response["message"]["content"])
