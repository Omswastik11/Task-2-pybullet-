import gym
import os
import cv2
import time as t
import numpy as np
import pybullet_workshop_23


CAR_LOCATION = [3,0,1.5]

BALL_LOCATION = [-3,0,1.5]

HUMANOID_LOCATION = [6,7,1.5]

VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})


os.chdir(os.path.dirname(os.getcwd()))
# Environment Setup ::---
env = gym.make('pybullet_workshop_23',
               arena="arena2",
               car_location=CAR_LOCATION,
               ball_location=BALL_LOCATION,
               humanoid_location=HUMANOID_LOCATION,
               visual_cam_settings=VISUAL_CAM_SETTINGS
               )

env.open_grip()
env.move(vels=[[6,6],
               [6,6]])
t.sleep(2.1)
env.move(vels=[[0,0],
               [0,0]])
env.close_grip()
t.sleep(1)
env.move(vels=[[2,-2],
               [2,-2]])

t.sleep(3.33)
env.move(vels=[[0,0],
               [0,0]])
env.close_grip()
t.sleep(1)
env.move(vels=[[7,7],
               [7,7]])
t.sleep(2.5)
env.move(vels=[[2,-2],
               [2,-2]])

t.sleep(3.75)
env.move(vels=[[0,0],
               [0,0]])
t.sleep(1)
while True:
    img = env.get_image(cam_height=0, dims=[512,512])
    cv2.imshow("img", img)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break
        env.open_grip()
        t.sleep(1)
        env.shoot()
        env.close_grip()
t.sleep(2)
env.close()
