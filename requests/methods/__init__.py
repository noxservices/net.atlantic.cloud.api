from apiurls import API_METHOD_URLS
from util import generate_url_data, read_api_url, get_seconds_since_epoch, \
    generate_rndguid, generate_signature
import urllib2
#-------------------------------------------------------------------------------
def describe_available_plan(version, acs_access_key_id, private_key, 
                            response_format, timestamp, rndguid, plan_name, 
                            platform):
    
    """
    This method enables the client to retrieve a list of available cloud server 
    plans & narrow the listing down optionally by server platform (windows, 
    linux, etc ) or get information about just one specific plan (e.g. extra 
    small plan XXS)
    """    
    
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    
    #add additional params
    url_data['plan_name'] = plan_name
    url_data['platform'] = platform
    
    return read_api_url(API_METHOD_URLS['describe-plan'], url_data)
#-------------------------------------------------------------------------------
def describe_image(version, acs_access_key_id, private_key, response_format,
                   timestamp, rndguid, imageid=""):
    """
    This method enables the client to retrieve a list of available cloud server 
    images & narrow the listing down optionally by a specific image.
    """
    
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    #add additional params
    if imageid:
        url_data['imageid'] = imageid
    return read_api_url(API_METHOD_URLS['describe-images'], url_data)
#-------------------------------------------------------------------------------
def list_instances(version, acs_access_key_id, private_key, response_format,
                   timestamp, rndguid):
    """
    This method enables the you to retrieve the list of currently active cloud 
    servers.
    """
    
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    return read_api_url(API_METHOD_URLS['list-instances'], url_data)
#-------------------------------------------------------------------------------
def run_instance(version, acs_access_key_id, private_key, response_format,
                 timestamp, rndguid, planname, imageid, server_qty, 
                 servername):
    """
    This method enables you to create new Cloud Servers by specifying a flexible 
    set of configuration parameters.
    """
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    url_data['planname'] = planname
    url_data['imageid'] = imageid
    url_data['server_qty'] = server_qty
    url_data['servername'] = servername
    
    return read_api_url(API_METHOD_URLS['run-instance'], url_data)
#-------------------------------------------------------------------------------
def describe_instance(version, acs_access_key_id, private_key, response_format,
                      timestamp, rndguid, instanceid):
    """
    This method enables the you to retrieve the details of a specific Cloud 
    Server.
    """
    
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    url_data['instanceid'] = instanceid
    return read_api_url(API_METHOD_URLS['describe-instance'], url_data)

#-------------------------------------------------------------------------------
def reboot_instance(version, acs_access_key_id, private_key, response_format,
                      timestamp, rndguid, instanceid, reboot_type):
    """
    This method enables the you to retrieve the details of a specific Cloud 
    Server.
    """
    
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    url_data['instanceid'] = instanceid
    url_data['RebootType'] = reboot_type
    
    return read_api_url(API_METHOD_URLS['reboot-instance'], url_data)
#-------------------------------------------------------------------------------
def terminate_instance(version, acs_access_key_id, private_key, response_format,
                      timestamp, rndguid, list_instances):
    """
    This method enables the you to retrieve the details of a specific Cloud 
    Server.
    """
    
    signature = generate_signature(timestamp, rndguid, private_key)
    url_data = generate_url_data(version, acs_access_key_id, response_format, 
                                 timestamp, rndguid, signature)
    for index, value in enumerate(list_instances):
        url_data['InstanceId_%s' % (index+1)] = value
        
    return read_api_url(API_METHOD_URLS['terminate-instance'], url_data)
#-------------------------------------------------------------------------------
if __name__=="__main__":
#    print describe_available_plan('XXS', 'linux', '2010-12-30', 
#                              'ATL64cdb70e4d3723a02dc401e87d3d119e', 
#                              '219579ec450e5aa7bb63d1f659c380916177cf9d',
#                              'xml', get_seconds_since_epoch(), 
#                               generate_rndguid())
#    
    
    
#    print describe_image('2010-12-30', 'ATL64cdb70e4d3723a02dc401e87d3d119e',
#                         '219579ec450e5aa7bb63d1f659c380916177cf9d', 'json',
#                         get_seconds_since_epoch(),generate_rndguid(),
#                         imageid="ubuntu-12.04_32bit" )


#    print list_instances('2010-12-30', 'ATL64cdb70e4d3723a02dc401e87d3d119e',
#                         '219579ec450e5aa7bb63d1f659c380916177cf9d', 'json',
#                         get_seconds_since_epoch(),generate_rndguid(),
#                          )

    print describe_instance('2010-12-30', 'ATL64cdb70e4d3723a02dc401e87d3d119e',
                         '219579ec450e5aa7bb63d1f659c380916177cf9d', 'json',
                         get_seconds_since_epoch(),generate_rndguid(),
                          20950)


