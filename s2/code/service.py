from aa274_s2.srv import Cat,CatResponse
import rospy

def handle_cat(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return CatResponse(req.a + req.b)

def cat_service():
    rospy.init_node('cat_service')
    s = rospy.Service('cat', Cat, handle_cat)
    rospy.spin()

if __name__ == "__main__":
    cat_service()
