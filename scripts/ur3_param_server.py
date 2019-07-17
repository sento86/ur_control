#!/usr/bin/python

import rospy

from dynamic_reconfigure.server import Server
from ur_control.cfg import demoConfig
   
def callback(config, level):
    rospy.loginfo("""Reconfigure Request: {int_param}, {double_param},\ 
            {str_param}, {bool_param}, {size}""".format(**config))
    return config
 
def main():
    rospy.init_node("ur3_param_server")

    srv = Server(demoConfig, callback)

    rospy.spin()

if __name__ == '__main__':
    main()
