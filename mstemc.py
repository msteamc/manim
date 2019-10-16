#!/usr/bin/env python

from manimlib.imports import *

from math import cos, sin, pi
import math
# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class Shapes1(Scene):
    def construct(self):
        ######code####
        #Making shapes
        circle = Circle()
        square = Square()
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]),
                           np.array([1, -1, 0]))

        #Showing shapes
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))


class Shapes(Scene):
    def construct(self):
        ####code#######
        #making shapes
        circle = Circle(color=YELLOW)
        square = Square(color=DARK_BLUE)
        square.surround(circle)

        rectangle = Rectangle(height=2, width=3, color=RED)
        ring = Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ring2 = Annulus(inner_radius=.6, outer_radius=1, color=BLUE)
        ring3 = Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ellipse = Ellipse(width=5, height=3, color=DARK_BLUE)

        pointers = []
        for i in range(8):
            pointers.append(
                Line(ORIGIN,
                     np.array([
                         cos(pi / 180 * 360 / 8 * i),
                         sin(pi / 180 * 360 / 8 * i), 0
                     ]),
                     color=YELLOW))

        # show animation
        self.add(circle)
        self.play(FadeIn(square))
        self.play(Transform(square, rectangle))
        self.play(FadeOut(circle), FadeIn(ring))
        self.play(Transform(ring, ring2))
        self.play(Transform(ring2, ring))
        self.play(FadeOut(square), GrowFromCenter(ellipse),
                  Transform(ring2, ring3))
        self.add(*pointers)
        self.wait(2)


class MakeText(Scene):
    def construct(self):
        ####Code#####
        #Making text
        first_line = TextMobject("Manim is fun")
        second_line = TextMobject("and useful")
        final_line = TextMobject("Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("Hope you like it too!")

        #coloring
        color_final_line.set_color_by_gradient(BLUE, PURPLE)

        #position text
        second_line.next_to(first_line, DOWN)

        #showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line),
                  ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)


class Equations(Scene):
    def construct(self):
        #Making equations
        first_eq = TextMobject(
            "$$ J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}]  $$"
        )
        second_eq = [
            "$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$",
            "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-",
            "$y^{(i)}$", "$)^2$"
        ]

        second_mob = TextMobject(*second_eq)

        for i, item in enumerate(second_mob):
            if (i != 0):
                item.next_to(second_mob[i - 1], RIGHT)

        eq2 = VGroup(*second_mob)

        des1 = TextMobject(
            "With manim, you can write complex equation like this...")
        des2 = TextMobject("Or this...")
        des3 = TextMobject("And it looks nice !!")

        #Coloring equations
        second_mob.set_color_by_gradient("#33ccff", "#ff00ff")

        #positioning equations
        des1.shift(2 * UP)
        des2.shift(2 * UP)
        #Animating equations
        self.play(Write(des1))
        self.play(Write(first_eq))
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(1)

        for i, item in enumerate(eq2):
            if (i < 2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00ffff")

        self.add(eq2)
        self.wait(1)
        self.play(FadeOutAndShiftDown(eq2), FadeOutAndShiftDown(first_eq),
                  Transform(des2, des3))
        self.wait(3)


class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label="X^{2}")

        func_graph_2 = self.get_graph(self.func_to_graph_2,
                                      self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label="x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,
                                                    func_graph,
                                                    color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x, y, color=YELLOW)

        point = Dot(self.coords_to_point(1, self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2),
                  Transform(graph_lab, graph_lab_2))
        self.wait(2)

    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph_2(self, x):
        return (x**3)


class ThreeDObjects(SpecialThreeDScene):
    def construct(self):
        sphere = self.get_sphere()
        cube = Cube()
        prism = Prism()
        self.play(ShowCreation(sphere))
        self.play(ReplacementTransform(sphere, cube))
        self.play(ReplacementTransform(cube, prism))
        self.wait(2)
