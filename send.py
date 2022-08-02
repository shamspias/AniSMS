from dotenv import load_dotenv
load_dotenv()
import os

import telnyx

class AniSMS:
    my_telnyx_number = "My Number"
    destination_number = "Number Want to Send"
    message_title = "Message Title"
    message_text = "Message Text"

    def send_sms(self, my_api_key):
        telnyx.api_key = my_api_key
        # print("My Sender Number is: ", self.my_telnyx_number)              
        # print("My API Key is: ", my_api_key)              
        # return telnyx.Message.create(
        #     from_=self.my_telnyx_number,
        #     to=self.destination_number,
        #     text=self.message_text,
        #     )
        try:
            return telnyx.Message.create(
                from_=self.my_telnyx_number,
                to=self.destination_number,
                text=self.message_text,
                )
        except:
            return False

# my_api_key = os.environ.get("TELNYX_SECRET_KEY")

# Get multiple api
file_handle_api_keys = open('api_list.txt', 'r')
api_key_list = file_handle_api_keys.readlines()
api_key_cnt = 1
my_api_key = api_key_list[0]
my_api_key = my_api_key.rstrip()
len_api_list = len(api_key_list) - 1


# Get multiple sender numbers
file_handle_sender_numbers = open('sender_number.txt', 'r')
sender_numbers_list = file_handle_sender_numbers.readlines()

# Massive number to send sms
file_handle_numbers = open('numbers.txt', 'r')
number_list = file_handle_numbers.readlines()
cnt = 0

sms_limit = int(input("Enter number of SMS for Each API: "))
sms_limit = sms_limit
limit = sms_limit

ani_sms = AniSMS()
ani_sms.my_telnyx_number = sender_numbers_list[0].rstrip()

my_message_text = input("Enter Your SMS: ") # MGS want to send

ani_sms.message_text = my_message_text

for i in number_list:

    print("Sending SMS TO: ",i)
    
    ani_sms.destination_number = i

    if cnt >= limit:
        print("Change API & Number")
        limit += sms_limit
        # because api key connected with sender number
        if api_key_cnt > len_api_list:
            print("Change back to 1st API again")
            api_key_cnt = 0
        ani_sms.my_telnyx_number = sender_numbers_list[api_key_cnt].rstrip()
        my_api_key = api_key_list[api_key_cnt].rstrip()
        api_key_cnt += 1
    cnt += 1
    

    for k in range(len_api_list*2):
        if ani_sms.send_sms(my_api_key):
            print("Send Successful")
            break

        else:
            print("Faild")
            print("Changing API & Number")
            if api_key_cnt > len_api_list:
                print("Changing back to 1st API again")
                api_key_cnt = 0
            # because api key connected with sender number
            ani_sms.my_telnyx_number = sender_numbers_list[api_key_cnt].rstrip()
            my_api_key = api_key_list[api_key_cnt].rstrip()
            api_key_cnt += 1