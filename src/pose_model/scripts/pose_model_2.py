#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA, Float32MultiArray
from geometry_msgs.msg import Quaternion, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray

markerArray = MarkerArray()

def callback(datax, datay, dataz):
    #global markerArray
    #coords = []
    markerArray = MarkerArray()
    for i in range(11):
	marker = Marker(
		header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
		ns="basic_shapes",
		id=i,
		type=Marker.CYLINDER,
		action=Marker.ADD,
		pose = Pose(datax[i], datay[i], dataz[i], Quaternion(0,0,1,0)),
		scale=Vector3(0.25, 0.25, 0.05),
		color=ColorRGBA(1, 0.5, 0.5, 1),
		lifetime=rospy.Duration()
	)
	
	markerArray.markers.append(marker)
        '''
	coords.append(data.poses[i].position)
	marker_line = Marker(
		header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
		ns="basic_shapes",
		id=100+i,
		type=Marker.LINE_STRIP,
		action=Marker.ADD,
		color=ColorRGBA(1, 1, 0, 1),
		points = coords,
		lifetime=rospy.Duration()
	)
	#marker_line.pose.orientation = (0, 1, 0, 0) #gives error
	marker_line.scale.x = 0.05 #gives 'keyword cannot be expression' error if put in ()
	
	markerArray.markers.append(marker_line)'''
    return markerArray

def main():
    #global markerArray
    rospy.init_node('basic_shapes', anonymous=True)    

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
    rospy.Subscriber('disks_posx', Float32MultiArray, callback)
    rospy.Subscriber('disks_posy', Float32MultiArray, callback)
    rospy.Subscriber('disks_posz', Float32MultiArray, callback)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
	markerPub.publish(marker())
	while markerPub.get_num_connections() < 1:
	    rospy.sleep(2)
	    rospy.logwarn("Please create a subscriber to the marker")

	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

