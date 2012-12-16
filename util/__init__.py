import base64
import hashlib
import hmac
import time
import urllib
import urllib2
import uuid

#-------------------------------------------------------------------------------
def get_seconds_since_epoch():
    """
    This method is used to return the current time in unix seconds 
    since epoch format.
    """
    
    return time.time()
#-------------------------------------------------------------------------------
def generate_rndguid():
    """
    This method is used to generate a randome sequence of characters.
    """
    
    return uuid.uuid4().__str__()
#-------------------------------------------------------------------------------
def generate_signature(timestamp, guid, private_key):
    """
    This method is used to generate a base64 encoded, hash of a Time Stamp and
    a randing GUID.
    """
    
    signature_string = "%s%s" % (timestamp, guid)
    digest = hmac.new(private_key, msg=signature_string, 
                         digestmod=hashlib.sha256).digest()
    return base64.b64encode(digest)
#-------------------------------------------------------------------------------
def encode_signature(signature):
    """
    This method is used to convert the hash signature obtained using 
    generate_signature() to a base64 encoded string.
    """
    
    return base64.b64encode(signature)
#-------------------------------------------------------------------------------
def generate_url_data(version, acs_access_key_id, response_format, timestamp, 
                      rndguid, signature):
    """
    This method returns a dictionary containing the required parameters used
    in the API request. 
    """
    
    return {
            'Version' : version,
            'ACSAccessKeyId' : acs_access_key_id,
            'Format' : response_format,
            'Timestamp' : timestamp,
            'Rndguid' : rndguid,
            'Signature' : signature
            }
#-------------------------------------------------------------------------------    
def read_api_url(url, data):
    """
    This method returns the response from reading a data url and the data provided
    as arguments to this method
    """
    
    data = urllib.urlencode(data)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    return response.read()
    
#-------------------------------------------------------------------------------    
if __name__ == "__main__":
    print generate_signature(time.time(), uuid.uuid4().__str__())