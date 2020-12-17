#!/usr/bin/env python
import rospy
from math import atan2
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)


def callback(data):
    print(data)
    msg = Twist()
    msg.linear.x = data.axes[1]
    # msg.linear.y = data.axes[1]
    msg.angular.z = 5*data.axes[2]



    pub.publish(msg)
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


if __name__ == '__main__':
    rospy.init_node('joy_listener', anonymous=True)
    rospy.Subscriber("joy", Joy, callback )
    rospy.spin()
