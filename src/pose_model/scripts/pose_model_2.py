#!/usr/bin/python
import rospy
from std_msgs.msg import Header, ColorRGBA, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray

markerArray = MarkerArray()
xcoords = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ycoords = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zcoords = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

xorien = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
yorien = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zorien = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
qorien = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def x_pos(x_pos):
    global xcoords
    xcoords = x_pos.data

def y_pos(y_pos):
    global ycoords
    ycoords = y_pos.data

def z_pos(z_pos):
    global zcoords
    zcoords = z_pos.data

def x_orien(x_orien):
    global xorien
    xorien = x_orien.data

def y_orien(y_orien):
    global yorien
    yorien = y_orien.data

def z_orien(z_orien):
    global zorien
    zorien = z_orien.data

def q_orien(q_orien):
    global qorien
    qorien = q_orien.data

def main():
    global xcoords, ycoords, zcoords, xorien, yorien, zorien, qorien
    rospy.init_node('pose_model', anonymous=True)

    markerPub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)
    rospy.Subscriber('disks_posx', Float32MultiArray, x_pos)
    rospy.Subscriber('disks_posy', Float32MultiArray, y_pos)
    rospy.Subscriber('disks_posz', Float32MultiArray, z_pos)

    rospy.Subscriber('disks_orienx', Float32MultiArray, x_orien)
    rospy.Subscriber('disks_orieny', Float32MultiArray, y_orien)
    rospy.Subscriber('disks_orienz', Float32MultiArray, z_orien)
    rospy.Subscriber('disks_orienq', Float32MultiArray, q_orien)

    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
	for i in range(11):
		marker = Marker(
			header=Header(frame_id="my_frame", stamp=rospy.Time.now()),
			ns="basic_shapes",
			id=i,
			type=Marker.CYLINDER,
			action=Marker.ADD,
			pose = Pose(Point(xcoords[i]/4, ycoords[i]/4, zcoords[i]/4), Quaternion(xorien[i], yorien[i], zorien[i], qorien[i])),
			scale=Vector3(0.5, 0.5, 0.1),
			color=ColorRGBA(1, 0.25, 1, 1),
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
