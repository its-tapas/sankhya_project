# core/consumers.py

import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class CustomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            # Accept the WebSocket connection
            await self.accept()
            logger.info("WebSocket connected.")
        except Exception as e:
            logger.error(f"Error during connect: {e}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            # Handle WebSocket disconnect logic
            logger.info(f"WebSocket disconnected: {close_code}")
        except Exception as e:
            logger.error(f"Error during disconnect: {e}")

    async def receive(self, text_data):
        try:
            # Handle received data and send a simple response
            logger.info(f"Received data: {text_data}")
            await self.send(text_data="Response")
        except Exception as e:
            logger.error(f"Error during receive: {e}")
