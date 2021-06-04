#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray

x_dot = 0.01
y_dot = 0.01
z_dot = 0.01
x_pos = 20.0
y_pos = 8.0
z_pos = 43.0

def joy_cb(data):
    global x_dot, y_dot, z_dot
    if data.buttons[4] == True:
	x_dot = data.axes[1]
	y_dot = data.axes[4]
	z_dot = data.axes[0]
    else:
	x_dot = 0
	y_dot = 0
	z_dot = 0

    return

def main():
    global x_dot, y_dot, z_dot
    rospy.init_node('parse_joystick_data', anonymous = True)
    rospy.Subscriber('joy', Joy, joy_cb)
    pos_pub = rospy.Publisher('instrument_pos', Float32MultiArray, queue_size=1)
    rate = rospy.Rate(10) #10hz

    while not rospy.is_shutdown():
	pos_data = Float32MultiArray()
	pos_data.data = [x_pos+x_dot, y_pos+y_dot, z_pos+z_dot]

	pos_pub.publish(pos_data)
	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

