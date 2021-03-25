#!/usr/bin/env python
import rospy

import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import PoseArray

def callback(data):
	br = tf2_ros.TransformBroadcaster()
	t = geometry_msgs.msg.TransformStamped()

	t.header.stamp = rospy.Time.now()
	t.header.frame_id = "my_frame"
	t.child_frame_id = "child"

	t.transform.translation = data.poses[0].position
	t.transform.rotation = data.poses[0].orientation

	br.sendTransform(t)

if __name__ == '__main__':
	rospy.init_node('world_frame')
	rospy.Subscriber('pose_array', PoseArray, callback)

	rospy.spin()
