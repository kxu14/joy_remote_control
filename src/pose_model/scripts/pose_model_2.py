#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray

xcoords = [1, 2, 3, 4, 5, 6]
ycoords = [1, 2, 3, 0, 0, 0]
zcoords = [1, 2, 3, 0, 0, 0]

def x_position(pos_data):
	global xcoords
    	xcoords = pos_data.data
	return

def y_position(data):
	global ycoords
    	ycoords = pos_data.data
	return

def z_position(data):
	global zcoords
    	zcoords = pos_data.data
	return

def main():
    global xcoords, ycoords, zcoords
    rospy.init_node('basic_shapes', anonymous=True)

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
    rospy.Subscriber('disks_posx', Float32MultiArray, x_position)
    rospy.Subscriber('disks_posy', Float32MultiArray, y_position)
    rospy.Subscriber('disks_posz', Float32MultiArray, z_position)
    rate = rospy.Rate(1)  # 1Hz

    markerArray = MarkerArray()

    while not rospy.is_shutdown():
	for i in range(11):
		marker = Marker(
			header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
			ns="basic_shapes",
			id=i,
			type=Marker.CYLINDER,
			action=Marker.ADD,
			pose = Pose(Point(xcoords[i], ycoords[i], zcoords[i]), Quaternion(0,0,1,0)),
			scale=Vector3(0.25, 0.25, 0.05),
			color=ColorRGBA(1, 0.5, 0.5, 1),
			lifetime=rospy.Duration()
		)
	
		markerArray.markers.append(marker)
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


'''
#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray


def callback(data): #, datay, dataz
    #coords = []
    markerArray = MarkerArray()
    for i in range(1,12):
	marker = Marker(
		header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
		ns="basic_shapes",
		id=i,
		type=Marker.CYLINDER,
		action=Marker.ADD,
		pose = Pose(Point(data.data[i], 0, i), Quaternion(0,0,1,0)),
		scale=Vector3(0.25, 0.25, 0.05),
		color=ColorRGBA(1, 0.5, 0.5, 1),
		lifetime=rospy.Duration()
	)
	
	markerArray.markers.append(marker)
        '''
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
	#marker_line.pose.orientation = (0, 1, 0, 0)
		#gives error, likely bc this is cpp syntax
	marker_line.scale.x = 0.05 #gives 'keyword cannot be expression' error if put in ()
	
	markerArray.markers.append(marker_line)'''
'''
    #return markerArray

def main():
    rospy.init_node('basic_shapes', anonymous=True)

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
    datax = rospy.Subscriber('disks_posx', Float32MultiArray, callback)
    #datay = rospy.Subscriber('disks_posy', Float32MultiArray, callback)
    #dataz = rospy.Subscriber('disks_posz', Float32MultiArray, callback)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
	markerPub.publish(markerArray) #callback()
	while markerPub.get_num_connections() < 1:
	    rospy.logwarn("Please create a subscriber to the marker")
	    rospy.sleep(1)

	rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

'''

