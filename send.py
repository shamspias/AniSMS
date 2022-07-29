from dotenv import load_dotenv
load_dotenv()
import os

import telnyx

class AniSMS:
    my_telnyx_number = "+18554834088"
    destination_number = "+16075480176"
    message_title = "Ani Test"
    message_text = "Hi It's check"

    def send_sms(self, my_api_key):
        telnyx.api_key = my_api_key
        return telnyx.Message.create(
            from_=self.my_telnyx_number,
            to=self.destination_number,
            text=self.message_text,
            )

# my_api_key = os.environ.get("TELNYX_SECRET_KEY")

# Get multiple api
file_handle_api_keys = open('api_list.txt', 'r')
api_key_list = file_handle_api_keys.readlines()
api_key_cnt = 0
my_api_key = api_key_list[api_key_cnt]

# Get multiple sender numbers
file_handle_sender_numbers = open('sender_number.txt', 'r')
sender_numbers_list = file_handle_sender_numbers.readlines()

# Massive number to send sms
file_handle_numbers = open('numbers.txt', 'r')
number_list = file_handle_numbers.readlines()
cnt = 0
limit = 6
ani_sms = AniSMS()

for i in number_list:
    print("Works Before send ",i)
    cnt += 1
    ani_sms.destination_number = i
    if cnt > limit:
        limit += 10
        api_key_cnt += 1

        # because api key connected with sender number
        ani_sms.my_telnyx_number = sender_numbers_list[api_key_cnt] 
        my_api_key = api_key_list[api_key_cnt]
        
    if ani_sms.send_sms(my_api_key):
        print("Send Successful")
    