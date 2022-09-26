import trycourier as tc
import time

client = tc.Courier(auth_token="pk_prod_ATMP66V9TF4A2BM0DRSXV7TWWP8J")

# time.sleep(5)

resp = client.send_message(
        message={
          "to": {
            "email": "adithyag020@gmail.com"
          },
          "content": {
            "title": "Welcome to Courier!",
            "body": "Want to hear a joke? {{joke}}"
          },
          "data":{
            "joke": "Why dothis is a test. I wanna see if stuff like this works"
          }
        }
      )