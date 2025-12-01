from manim import *

class AlgorithmVisualization(Scene):
    def construct(self):
        # Title and initial data setup
        title = Text("Bubble Sort", font_size=48).to_edge(UP)
        self.play(Write(title))

        data = [8, 3, 1, 7, 0, 10, 2]
        n = len(data)

        # Create visual representation of the array
        squares = VGroup()
        for val in data:
            square = Square(side_length=1.0)
            number = Text(str(val), font_size=32).move_to(square.get_center())
            element = VGroup(square, number)
            squares.add(element)
        
        squares.arrange(RIGHT, buff=0.5).shift(UP * 0.5)
        
        # Store the fixed screen positions for elements to move to during swaps
        positions = [sq.get_center().copy() for sq in squares]

        self.play(Create(squares))
        self.wait(1)

        # Pointers to indicate elements being compared
        pointer1 = Arrow(start=UP, end=DOWN, color=YELLOW).scale(0.6)
        pointer2 = Arrow(start=UP, end=DOWN, color=ORANGE).scale(0.6)

        # Updatable text for status messages
        pass_text = Text("", font_size=36).to_edge(DOWN, buff=1.0)
        status_text = Text("", font_size=28).next_to(squares, DOWN, buff=1.0)
        self.add(pass_text, status_text)

        # Bubble Sort Algorithm Visualization
        for i in range(n - 1):
            self.play(pass_text.animate.set_text(f"Pass {i + 1}"))
            
            for j in range(n - 1 - i):
                # Animate pointers to position and highlight elements
                animations = [
                    squares[j][0].animate.set_color(YELLOW),
                    squares[j+1][0].animate.set_color(ORANGE)
                ]
                if i == 0 and j == 0:
                    pointer1.next_to(squares[j], DOWN, buff=0.2)
                    pointer2.next_to(squares[j+1], DOWN, buff=0.2)
                    animations.extend([FadeIn(pointer1), FadeIn(pointer2)])
                else:
                    animations.extend([
                        pointer1.animate.next_to(squares[j], DOWN, buff=0.2),
                        pointer2.animate.next_to(squares[j+1], DOWN, buff=0.2)
                    ])
                self.play(*animations, run_time=0.5)
                self.wait(0.2)

                # Perform comparison
                if data[j] > data[j+1]:
                    # Swap is needed
                    self.play(status_text.animate.set_text(f"{data[j]} > {data[j+1]} -> Swap"))

                    # Animate the swap of the VGroups
                    self.play(
                        squares[j].animate.move_to(positions[j+1]),
                        squares[j+1].animate.move_to(positions[j]),
                        run_time=1.0
                    )
                    
                    # Update the data array and the VGroup order to match
                    data[j], data[j+1] = data[j+1], data[j]
                    squares[j], squares[j+1] = squares[j+1], squares[j]
                    
                else:
                    # No swap needed
                    self.play(status_text.animate.set_text(f"{data[j]} <= {data[j+1]} -> No Swap"))
                    self.wait(0.5)

                # Unhighlight elements and clear the status text
                self.play(
                    squares[j][0].animate.set_color(WHITE),
                    squares[j+1][0].animate.set_color(WHITE),
                    status_text.animate.set_text(""),
                    run_time=0.5
                )

            # Mark the element at the end of the pass as sorted
            self.play(squares[n - 1 - i][0].animate.set_color(GREEN))

        # Mark the first element as sorted
        self.play(squares[0][0].animate.set_color(GREEN))
        self.wait(0.5)

        # Final cleanup and message
        self.play(FadeOut(pointer1, pointer2))
        self.play(pass_text.animate.set_text("Array is Sorted!"), FadeOut(status_text))
        self.wait(3)