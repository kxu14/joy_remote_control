#!/usr/bin/env python

import roslib; roslib.load_manifest('rviz')
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray
import rospy

topic = 'test_poses'
publisher = rospy.Publisher("pose_array", PoseArray, queue_size = 10)

rospy.init_node('posearray')

while not rospy.is_shutdown():

   ps = PoseArray()
   ps.header.frame_id = "/base_link"
   ps.header.stamp = rospy.Time.now()
   
   pose = Pose()
   pose.position.x = 2
   pose.position.y = 2
   pose.position.z = 0
   pose.orientation.x = 0
   pose.orientation.y = 0.7071
   pose.orientation.z = 0.7071
   pose.orientation.w = 0

   ps.poses.append( pose )

   pose = Pose()
   pose.position.x = 1
   pose.position.y = 1
   pose.position.z = 0
   pose.orientation.x = 0
   pose.orientation.y = 1
   pose.orientation.z = 0
   pose.orientation.w = 0

   ps.poses.append( pose )

   publisher.publish( ps )

   rospy.sleep(0.1)
