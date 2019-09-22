from aa274_s2.srv import Cat,CatResponse
import rospy
import sys

def cat_client(x, y):
    rospy.wait_for_service('cat')
    try:
        cat_proxy = rospy.ServiceProxy('cat', Cat)
        resp1 = cat_proxy(x, y)
        return resp1.cat
    except rospy.ServiceException, e:
        print("Service call failed")

if __name__ == "__main__":
	s1 = "hi"
	s2 = "hello"
	result = cat_client(s1,s2)
	print(result)
