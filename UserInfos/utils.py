from .models import UserInfo


#   WARNING: Don't delete unused parameter.
def jwt_response_payload_handler(token, user=UserInfo, request=None):
    return {
        'token': token,
        'user_id': user.UserId
    }


'''
Calculate euclidean distance, 
return True if two points are in the standard range
return False if two points are not in the range
'''


def euclidean_distance(p1_lat, p1_long, p2_lat, p2_long):
    standard_distance = 1**2
    dis_lat = p1_lat - p2_lat
    dis_long = p1_long - p2_long
    distance = dis_lat**2 + dis_long**2
    if distance <= standard_distance:
        return True
    return False

