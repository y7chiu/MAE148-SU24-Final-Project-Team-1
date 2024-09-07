#!/usr/bin/python3
import rospy
import tf
import tf.transformations
from nav_msgs.msg import Odometry

def handle_odometry(msg):
    # Create a TransformBroadcaster object
    br = tf.TransformBroadcaster()

    # Get the position from the odometry message
    position = msg.pose.pose.position

    # Get the orientation from the odometry message (as a quaternion)
    orientation = msg.pose.pose.orientation

    # Convert the odometry quaternion to a list
    original_quaternion = [orientation.x, orientation.y, orientation.z, orientation.w]

    # Define a 180-degree rotation around the Z-axis (z-axis flip)
    z_flip_quaternion = tf.transformations.quaternion_from_euler(0, 0, 3.14159)  # 180 degrees in radians

    # Apply the 180-degree rotation to the original orientation (quaternion multiplication)
    flipped_orientation = tf.transformations.quaternion_multiply(original_quaternion, z_flip_quaternion)

    # Broadcast the transform from odom -> base_link, with the flipped orientation
    br.sendTransform((position.x, position.y, position.z),
                     flipped_orientation,
                     rospy.Time.now(),
                     "base_link",  # child frame (the robot's base)
                     "odom")       # parent frame (odometry frame)

if __name__ == '__main__':
    rospy.init_node('odom_to_tf_broadcaster')

    # Subscribe to the odometry topic (replace '/odom' with your actual topic)
    rospy.Subscriber('/odom', Odometry, handle_odometry)

    rospy.spin()
