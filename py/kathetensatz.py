from manim import *
import numpy as np

from modules.data_write import write_data

# PARAMETERS

r = 2
angle = np.pi*2/5
rt = 3

# colours
colour_tri = "#5be800"
colour_quad = "#0777ba"

common_kwargs = {"fill_opacity": 0.5}


class Kathetensatz(Scene):
    meta_data = {
        "title": "Kathetensatz",
        "timestamps": [0],
        "filename": "Kathetensatz.mp4",
        "path": "videos/"
    }

    def draw_logo(self):
        self.add(SVGMobject("stz-white.svg").scale_to_fit_width(0.3).to_corner(corner=RIGHT + DOWN))

        
    def add_timestamp(self):
        self.meta_data["timestamps"].append(self.renderer.time)

    def construct(self):
        self.draw_logo()
        # Parameters
        pa = np.array([-r, 0, 0])
        pb = np.array([r, 0, 0])
        pc = np.array([r*np.cos(angle), r*np.sin(angle), 0])
        a = np.sqrt((pc[0]-pb[0])**2 + pc[1]**2)
        triangle = Polygon(pa, pb, pc, color=colour_tri, **common_kwargs)
        self.add(triangle)

        t_tracker = ValueTracker(0)
        p1 = pb
        p2 = pb + a*np.array([np.cos(angle/2), np.sin(angle/2), 0])
        p3_0 = p2 + pc - pb
        p4_0 = pc
        square = Polygon(p1, p2, p3_0, p4_0, color=colour_quad, **common_kwargs)

        # animation updater

        square.add_updater(
            lambda x: x.become(Polygon(p1, p2, p3_0 + (pa - pc)*t_tracker.get_value(), p4_0 + (pa - pc)*t_tracker.get_value(), color=colour_quad, **common_kwargs))
        )
        self.add(square)
        self.play(t_tracker.animate.increment_value(1), run_time=rt)
        self.add_timestamp()

        angle_tracker = ValueTracker(0)
        p4 = pa
        p3 = p4 + p2-p1
        p3d = p3 - p1
        square.add_updater(
            lambda x: x.become(Polygon(pb, pb + a*np.array([np.cos(angle/2 + angle_tracker.get_value()), np.sin(angle/2 + angle_tracker.get_value()), 0]),
                                p1 + np.array([p3d[0]*np.cos(angle_tracker.get_value())-p3d[1]*np.sin(angle_tracker.get_value()),
                                 p3d[0]*np.sin(angle_tracker.get_value())+p3d[1]*np.cos(angle_tracker.get_value()),0]),
                                pb + 2*r*np.array([-np.cos(angle_tracker.get_value()), -np.sin(angle_tracker.get_value()), 0]),
                                color=colour_quad, **common_kwargs))
        )
        self.play(angle_tracker.animate.increment_value(np.pi/2), run_time=rt)
        self.add_timestamp()
        

        p2 = pc
        p3 = pc + np.array([0, -2*r, 0])
        p4 = p1 + np.array([0, -2*r, 0])

        s_tracker = ValueTracker(0)
        square.add_updater(
            lambda x: x.become(Polygon(p1, p2*np.array([1, 1-s_tracker.get_value(), 1]), p2*np.array([1, 1-s_tracker.get_value(), 1])-np.array([0, 2*r, 0]), p4,
                                color=colour_quad, **common_kwargs))
        )
        self.play(s_tracker.animate.increment_value(1), run_time=rt)
        self.add_timestamp()
        
        write_data(self.meta_data)
