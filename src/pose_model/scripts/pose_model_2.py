#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Quaternion, PoseArray, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray

markerArray = MarkerArray()

def callback(data):
    global markerArray
    for i in range(len(data.poses)):
	marker = Marker(
		header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
		ns="basic_shapes",
		id=i,
		type=Marker.CYLINDER,
		action=Marker.ADD,
		pose=data.poses[i],
		scale=Vector3(0.25, 0.25, 0.05),
		color=ColorRGBA(0.65, .6, 1, 1),
		lifetime=rospy.Duration()
	)
	
	markerArray.markers.append(marker)
	break

def main():
    global markerArray
    rospy.init_node('basic_shapes', anonymous=True)    

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
    rospy.Subscriber('pose_array', PoseArray, callback)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
	markerPub.publish(markerArray)
	while markerPub.get_num_connections() < 1:
	    rospy.logwarn("Please create a subscriber to the marker")
	    rospy.sleep(1)

	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

