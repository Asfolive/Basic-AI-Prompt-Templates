from openai import OpenAI


client = OpenAI(
    api_key='DIGITE API_KEY OPEN AI'
)

response = client.images.generate(
    model='dall-e-3',
    prompt='um programador com seu laptop, no estilo futurista',
    size='1024x1024',
    quality='standard',
    n=1,
)
image_url = response.data[0].url
print(image_url)

