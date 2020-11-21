#!/usr/bin/env python3
from discord_webhooks import DiscordWebhooks
import time

class Discord:
    def __init__(self, wurl):
        self.webhook_url = wurl

    def send_msg(self, title, desc, msg_title, msg):
        time.sleep(3)
        webhook = DiscordWebhooks(self.webhook_url)
        webhook.set_footer(text='    --By Hariprasath')
        webhook.set_content(title=title, description=desc)
        webhook.add_field(name=msg_title, value=msg)
        webhook.send()
    
    def msg(self, msg):
        webhook = DiscordWebhooks(self.webhook_url)
        webhook.add_field(name="Error", value=msg)
        webhook.send()