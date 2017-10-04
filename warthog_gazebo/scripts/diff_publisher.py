#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

def publish_dummy_diffs():
  jsm = JointState()
  joint_names = ['left_diff_unit_jnt', 'right_diff_unit_jnt']
  joint_values = [0.0, 0.0]
  jsm.name = joint_names
  jsm.position = joint_values

  rospy.init_node('diff_joint_state_publisher', anonymous=True)
  rate = rospy.Rate(10)

  joint_states_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

  while not rospy.is_shutdown():
      jsm.header.stamp = rospy.Time.now()
      joint_states_pub.publish(jsm)
      rate.sleep()

if __name__ == '__main__':
  publish_dummy_diffs()
