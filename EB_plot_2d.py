from manimlib.imports import *


class Plot1(GraphScene):
    CONFIG = {
        "y_max": 50,
        "y_min": 0,
        "x_max": 7,
        "x_min": 0,
        "y_tick_frequency": 5,
        "x_tick_frequency": 0.5,
        "axes_color": BLUE,
        "y_labeled_nums": range(0, 60, 10),
        "x_labeled_nums": list(np.arange(2, 7.0 + 0.5, 0.5)),
        "x_label_decimal": 1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal": 3
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x**2, color=GREEN, x_min=2, x_max=4)
        self.play(ShowCreation(graph), run_time=2)
        self.wait()


class Plot1v2(GraphScene):
    CONFIG = {
        "y_max": 50,
        "y_min": 0,
        "x_max": 7,
        "x_min": 0,
        "y_tick_frequency": 5,
        "x_tick_frequency": 1,
        "axes_color": BLUE,
        "graph_origin": np.array((0, 0, 0))
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x**2, color=GREEN, x_min=2, x_max=4)
        self.play(ShowCreation(graph), run_time=2)
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$f(t)$",
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = 2
        end_label_x = 7
        step_x = 1
        #   For y
        init_label_y = 20
        end_label_y = 50
        step_y = 5
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )
