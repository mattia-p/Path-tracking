# -*- coding: utf-8 -*-
"""
@author: mattia
"""
import numpy as np
import matplotlib.pyplot as plt

class TrackedPathPlotter():
    """
    Used for plotting the path
    """

    @staticmethod
    def path_visualizer(traj_x, traj_y, X_0, X_goal):
        """
        Simple plot for visualizing the trajectory
        """

        plt.plot(traj_x, traj_y)
        plt.plot(X_goal[0], X_goal[1], 'ro', label='Target')
        plt.arrow(X_0[0],X_0[1], 1.5 * np.cos(X_0[2]), 1.5 * np.sin(X_0[2]),head_width=0.4, head_length=0.5, length_includes_head=True,width=0.09, color = 'black')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim([min(X_0[0],X_goal[0]) - 5, max(X_0[0],X_goal[0]) + 5])
        plt.ylim([min(X_0[1],X_goal[1]) - 5, max(X_0[1],X_goal[1]) + 5])
        plt.minorticks_on()
        plt.grid(b=True, which='major', color='black', linestyle='-', linewidth=0.5)
        plt.grid(b=True, which='minor', color='black', linestyle='--', linewidth=0.2)

        plt.ion()
        plt.show()
        raw_input("Press Enter to close plot...")
        plt.close()
