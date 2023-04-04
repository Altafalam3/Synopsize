import requests
import xml.etree.ElementTree as ET


def summarise(text):

    # Set the URL of your webhook
    webhook_url = 'https://what-the-gpt.vercel.app/api/message'

    # Set the message you want to send to the webhook

    message = text + '     Can you summarize this text?'

    # Set the JSON payload to be sent with the request
    payload = {'Body': message}

    print(message)

    # Send the POST request to the webhook with the payload
    response = requests.post(webhook_url, json=payload)

    # Parse the XML and get the message element text
    root = ET.fromstring(response.text)
    response_message = root.find('Message').text

    # Print the response message
    print(response_message)
    responseMessage = response_message.strip()
    return responseMessage