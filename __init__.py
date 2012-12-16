from util import generate_signature, get_seconds_since_epoch, generate_guid, \
    encode_signature


#make a request

#get encoded signature

signature = generate_signature(get_seconds_since_epoch(), 
                                       generate_guid())

encoded_signature = "YTczMmQ4ZjUyZTMxYWMxNGI4MTljNjg2MTE4MmExMzc2MTJkNzBlZDg4NmRmNTI5MDkxYWU1NjNhNDk0MDRjMA==" #encode_signature(signature)

print encoded_signature



