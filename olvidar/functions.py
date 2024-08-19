import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def refresh_google_token():
    creds = None
    # Verificar si el archivo de token ya existe
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Si las credenciales están caducadas, intenta refrescarlas
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        except Exception as e:
            print(f'Error refreshing token: {e}')
            creds = None
    # Si no hay credenciales válidas, obtener nuevas credenciales
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

def send_mail_google(to_email, subject, message_text):
    refresh_google_token()  # Asegurarse de que el token está actualizado

    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(message_text)
        message['to'] = to_email
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {'raw': raw_message}

        sent_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f'Message Id: {sent_message["id"]}')
        return True
    except HttpError as error:
        print(f'An error occurred: {error}')
        return False


