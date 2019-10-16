from manimlib.imports import *

COLOR_P = "#3EFC24"


class TextColor(Scene):
    def construct(self):
        text = TextMobject("A", "B", "C", "D", "E", "F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)


class FormulaColor1(Scene):
    def construct(self):
        text = TexMobject("x", "=", "{a", "\\over", "b")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        self.play(Write(text))
        self.wait(2)


class FormulaColor3(Scene):
    def construct(self):
        text = TexMobject("\\sqrt{", "\\int_{", "a}^", "{b}", "\\left(",
                          "\\frac{x}{y}", "\\right)", "dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)


class FormulaColor3fixed(Scene):
    def construct(self):
        text = TexMobject("\\sqrt{", "\\int_{", "a}^", "{b}", "\\left(",
                          "\\frac{x}{y}", "\\right)", "dx.}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)


class FormulaColor3fixed2(Scene):
    def construct(self):
        text = TexMobject("\\sqrt{", "\\int_{", "a}^", "{b}", "\\left(",
                          "\\frac{x}{y}", "\\right)", "d", "x", ".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(8)


class FormulaColor5(Scene):
    def construct(self):
        text = TexMobject("\\sqrt{", "\\int_", "{a", "+", "c}^", "{b}",
                          "{\\left(", "{x", "\\over", "y}", "\\right)}", "d",
                          "x", ".}")
        for i, color in zip(text, [PURPLE, BLUE, GREEN, YELLOW, PINK]):
            i.set_color(color)
        self.play(Write(text))
        self.wait(3)


class ColorByCaracter(Scene):
    def construct(self):
        text = TexMobject("{d", "\\over", "d", "x", "}", "\\int_", "{a}^", "{",
                          "x", "}", "f(", "t", ")d", "t", "=", "f(", "x", ")")
        text.set_color_by_tex("x", RED)
        self.play(FadeIn(text))
        self.wait(5)


class ColorByCaracterFixed(Scene):
    def construct(self):
        text = TexMobject("{d", "\\over", "d", "x", "}", "\\int_", "{a}^", "{",
                          "x", "}", "f(", "t", ")d", "t", "=", "f(", "x", ")")
        text.set_color_by_tex("x", RED)
        text[6].set_color(RED)
        text[8].set_color(WHITE)
        self.play(FadeIn(text))
        self.wait(5)


class ListFor(Scene):
    def construct(self):
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]",
                          "[7]")
        for i in [0, 1, 3, 4]:
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)


class ForRange1(Scene):
    def construct(self):
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]",
                          "[7]", "[8]")
        for i in range(3):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)


class ForRange2(Scene):
    def construct(self):
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]",
                          "[7]")
        for i in range(2, 6):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)


class ForTwoVariables(Scene):
    def construct(self):
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]",
                          "[7]")
        for i, color in [(2, RED), (4, PINK)]:
            text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)


class ChangeSize(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=0}^n i = \\frac{n(n+1)}{2}")
        self.add(text)
        self.wait(3)
        text.scale_in_place(2)
        self.play(Write(text))
        self.wait(3)


class AddAndRemoveText(Scene):
    def construct(self):
        text = TextMobject("Text Or object")
        self.wait()
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()


class FadeText(Scene):
    def construct(self):
        text = TextMobject("Text or Object")
        self.play(FadeIn(text), run_time=5)
        self.wait()
        self.play(FadeOut(text), run_time=5)
        self.wait()

class FadeTextDirection(Scene):
    def construct(self):
