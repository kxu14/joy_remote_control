#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32MultiArray

x_dot = 0.0
y_dot = 0.0
z_dot = 0.0

def joy_cb(data):
    global x_dot
    global y_dot
    global z_dot

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
    global x_dot
    global y_dot
    global z_dot

    rospy.init_node('parse_joystick_data', anonymous = True)
    rospy.Subscriber('joy', Joy, joy_cb)
    v_dot_pub = rospy.Publisher('instrument_vel', Float32MultiArray, queue_size=1)
    
    rate = rospy.Rate(10) #10hz

    while not rospy.is_shutdown():
	v_dot_data = Float32MultiArray()
	v_dot_data.data = [x_dot, y_dot, z_dot]

	v_dot_pub.publish(v_dot_data)
	rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

