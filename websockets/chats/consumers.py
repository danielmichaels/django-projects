import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # here we can do auth before accepting the connection
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        # always call this last to ensure we've done all checks
        await self.accept()

    async def disconnect(self, code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # rx msg from websocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # rx msg from room group
    async def chat_message(self, event):
        message = event["message"]

        # send msg to websocket
        await self.send(text_data=json.dumps({"message": message}))
