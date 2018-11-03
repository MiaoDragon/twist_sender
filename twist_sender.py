#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#added
from geometry_msgs.msg import Twist

rospy.init_node('twist_sender', anonymous=True)
msg = Twist()
pub = rospy.Publisher('cmd_vel', Twist)
while not rospy.is_shutdown():
    msg.linear.x = 2.
    msg.linear.y = 0.
    msg.linear.z = 0.
    msg.angular.x = 0.
    msg.angular.y = 0.
    msg.angular.z = 1.
    speed = 0.4
    pub.publish(msg)
