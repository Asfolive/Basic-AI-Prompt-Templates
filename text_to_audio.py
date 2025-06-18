from openai import OpenAI


client = OpenAI(
    api_key='DIGITE API_KEY OPEN AI'
)

response = client.audio.speech.create(
    model='tts-1',
    voice='nova',
    input='Estou gostando muito de utilizar inteligencia artificial',
)

response.write_to_file('meu_audio.mp3')

