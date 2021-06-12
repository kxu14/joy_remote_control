#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray

markerArray = MarkerArray()
xcoords = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ycoords = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zcoords = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def x_pos_cb(x_pos_data):
    global xcoords
    xcoords = x_pos_data.data
    '''print x_pos_data.data
    print xcoords
    print xcoords[4]'''

def y_pos_cb(y_pos_data):
    global ycoords
    ycoords = y_pos_data.data

def z_pos_cb(z_pos_data):
    global zcoords
    zcoords = z_pos_data.data

def main():
    global xcoords, ycoords, zcoords
    rospy.init_node('pose_model', anonymous=True)

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
    rospy.Subscriber('disks_posx', Float32MultiArray, x_pos_cb)
    rospy.Subscriber('disks_posy', Float32MultiArray, y_pos_cb)
    rospy.Subscriber('disks_posz', Float32MultiArray, z_pos_cb)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
	for i in range(11):
		marker = Marker(
			header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
			ns="basic_shapes",
			id=i,
			type=Marker.CYLINDER,
			action=Marker.ADD,
			pose = Pose(Point(xcoords[i], ycoords[i], zcoords[i]), Quaternion(0,0,1,0)),
			scale=Vector3(0.5, 0.5, 0.1),
			color=ColorRGBA(0, 1, 0, 1),
			lifetime=rospy.Duration()
		)
	
		markerArray.markers.append(marker)
	markerPub.publish(markerArray)

	while markerPub.get_num_connections() < 1:
	    rospy.logwarn("Please create a subscriber to the marker")
	    rospy.sleep(5)

	rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
