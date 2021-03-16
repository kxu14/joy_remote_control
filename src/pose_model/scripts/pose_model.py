#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray

def marker():
	markerArray = MarkerArray()
	for i in range (0,10):
		marker = Marker(
			header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
			ns="basic_shapes",
			id=i,
			type=Marker.CYLINDER,
			action=Marker.ADD,
			pose=Pose(Point(0, 0, i), Quaternion(0, 0, 0, 1)),
			scale=Vector3(0.5, 0.5, 0.25),
			color=ColorRGBA(0.65, .6, 1, 1),
			lifetime=rospy.Duration()
		)
		
		markerArray.markers.append(marker)
	#markerPub.publish(markerArray) <-- CANT DO THIS, DOESNT DISPLAY
	return markerArray

def main():
    rospy.init_node('basic_shapes', anonymous=True)

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
		#name of publisher cannot change
    #rospy.Subscriber('pose_array', PoseArray, callback)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
	markerPub.publish(marker())
	while markerPub.get_num_connections() < 1:
	    rospy.logwarn("Please create a subscriber to the marker")
	    rospy.sleep(1)

	rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


