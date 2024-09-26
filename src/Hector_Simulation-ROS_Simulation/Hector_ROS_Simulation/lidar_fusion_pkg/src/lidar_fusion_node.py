#!/usr/bin/env python3

import rospy 
from sensor_msgs.msg import LaserScan 

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " LiDAR data received: %s", data.ranges)

def lidar_fusion():
    rospy.init_node('lidar_fusion_node', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_fusion()
    except rospy.ROSInterruptException:
        pass 