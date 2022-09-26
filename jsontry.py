# import json

# # with  open('users.json') as json_file:
# #     data  = json.load(json_file)

# # print(data)


# def write_json(new_data, filename='donor.json'):
#     with open(filename,'r+') as file:
#           # First we load existing data into a dict.
#         file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#         file_data.append(new_data)
#         # Sets file's current position at offset.
#         file.seek(0)
#         # convert back to json.
#         json.dump(file_data, file, indent = 4)
#         print(file_data)
#         print(type(file_data))



# with open('donor.json') as json_file:
#             data  = json.load(json_file)

# for i in data:
#     print(i["email"])






# # y = {"emp_name":"Nikhil",
# #      "email": "nikhil@geeksforgeeks.org",
# #      "job_profile": "Full Time"
# #     }
     
# # write_json(y)

# # a = [1,2,3]
# # print(type(a))





# import trycourier as tc
# import time

# client = tc.Courier(auth_token="pk_prod_ATMP66V9TF4A2BM0DRSXV7TWWP8J")

# # time.sleep(2)

# resp = client.send_message(
#         message={
#           "to": {
#             "email": "adithyag020@gmail.com"
#           },
#           "content": {
#             "title": "Welcomkfyfvyihhilfdigfigfhiofe to Courier!",
#             "body": "Want to hear a joke? {{joke}}"
#           },
#           "data":{
#             "joke": "Why dotdytnhxtfjutxjtjut"
#           }
#         }
#       )



# from serpapi import GoogleSearch

# params = {
#   "api_key": "17c5b1871ac410368c258a7985181f724a0c2da4737664bab80710da79dc7421",
#   "engine": "google_maps",
#   "type": "search",
#   "google_domain": "google.com",
#   "q": "pes university",
#   "hl": "en",
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# # print(results)
# print(results["search_metadata"]["google_maps_url"])



import json
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
with open("logged.json", "w") as outfile:
    json.dump(dictionary, outfile)

with  open('logged.json') as json_file:
    data  = json.load(json_file)

print(data["name"])