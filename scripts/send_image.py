import rospy
import cv2
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def main():

    print "creating ROS msg from image"
    rospy.init_node("ML_node", anonymous=True)
    pub = rospy.Publisher("/debug_image", Image)
    time.sleep(2)

    # jpg -> cv2
    print "converting jpg"
    image = cv2.imread("/home/user/image.jpg", cv2.IMREAD_COLOR)

    # cv2 -> ROS imgmsg
    print "converting cv2"
    msg = CvBridge().cv2_to_imgmsg(image, encoding="passthrough")

    print "sending to topic"
    while 1:
        pub.publish(msg)

if __name__ == '__main__':
    main()
