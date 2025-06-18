from openai import OpenAI


client = OpenAI(
    api_key='DIGITE API_KEY OPEN AI'
)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Voce é um assistente virtual especializado em python e desenvolvimento. Dê respostas técnicas sobre programação.'
        },
   
        {
            'role': 'user',
            'content': 'Me fale mais sobre a historia do python'
        },
    ],
    
    max_tokens=300,
    temperature=0.2,
)



#Caso queira alterar o tipo de recebimento de dados, em bloco unico ou estilo chatgpt mandando as respostas aos poucos
#stream = client.chat.completions.create(
#    model='gpt-3.5-turbo',
#    messages=[
#        {'role': 'user', 'content': 'Me fale mais sobre o flutter'},
#    ],
#    stream=True, #receber a resposta aos poucos
#)
#for chunk in stream:
#    if chunk.choices[0].delta.content is not None:
#        print(chunk.choices[0].delta.content, end='')



print(response.choices[0].message.content)