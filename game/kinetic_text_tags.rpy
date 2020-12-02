"""
 Kinetic Text Tags Ren'Py Module
 2020 Daniel Westfall <SoDaRa2595@gmail.com>


 http://twitter.com/sodara9
 I don't really have much to plug. Never made much of note before.
 But I'd appreciate being given credit if you do end up using it! :D Would really
 make my day to know I helped some people out!
 Really hope this can help the community create some really neat ways to spice
 up their dialogue!
 http://opensource.org/licenses/mit-license.php
 Forum Post: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=60527&sid=75b4eb1aa5212a33cbfe9b0354e5376b
 Github: https://github.com/SoDaRa/Kinetic-Text-Tags
"""
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


##### Our preference to disable the chaos text #####
default gui.chaos_on = False  # You can change this to be gui.chaos_text or persistent.chaos_text if you'd prefer.

init python:

    import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        def __init__(self):
            self.alpha = None
            self.font = None
            self.size = None
            self.bold = False
            self.italic = False
            self.underline = False
            self.strikethrough = False
            self.plain = False
            self.color = None
            self.user_style = None
            self.outline_color = None
            # Be sure to add your own tags here if you want to wrap them up in each other
            # I advise assigning None if they take an argument and False if they don't
            # Be careful of the order tags are applied. Any tag meant to manipulate text
            # should be the innermost one.
            self.bounce_tag = None
            self.fade_in_tag = None
            self.scare_tag = None
            self.rotate_tag = None
            self.chaos_tag = False
            self.move_tag = False
            self.omega_tag = None



        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Stole this from Text(). Mostly just want to get the tag info
            #Common Tags
            if tag == "b":
                self.bold = True
                return True
            elif tag == "/b":
                self.bold = False
                return True

            elif tag == "s":
                self.strikethrough = True
                return True
            elif tag == "/s":
                self.strikethrough = False
                return True

            elif tag == "u":
                self.underline = True
                return True
            elif tag == "/u":
                self.underline = False
                return True

            elif tag == "i":
                self.italic = True
                return True
            elif tag == "/i":
                self.italic = False
                return True

            #Be sure to copy the parameters for any tag that has arguments!!
            elif tag == "color":
                self.color = char
                return True
            elif tag == "/color":
                self.color = None
                return True

            elif tag == "alpha":
                self.alpha = char
                return True
            elif tag == "/alpha":
                self.alpha = None
                return True

            elif tag == "font":
                self.font = char
                return True
            elif tag == "/font":
                self.font = None
                return True

            elif tag == "":
                self.user_style = char
                return True
            elif tag == "/":
                self.user_style = None
                return True

            elif tag == "size":
                self.size = char
                return True
            elif tag == "/size":
                self.size = None
                return True

            elif tag == "outlinecolor":
                self.outline_color = char
                return True
            elif tag == "/outlinecolor":
                self.outline_color = None
                return True

            elif tag == "plain":
                self.plain = True
                return True
            elif tag == "/plain":
                self.plain = False
                return True

            #Custom Tags
            elif tag == "bt":
                self.bounce_tag = char
                return True
            elif tag == "/bt":
                self.bounce_tag = None
                return True

            elif tag == "fi":
                self.fade_in_tag = char
                return True
            elif tag == "/fi":
                self.fade_in_tag = None
                return True

            elif tag == "sc":
                self.scare_tag = char
                return True
            elif tag == "/sc":
                self.scare_tag = None
                return True

            elif tag == "rotat":
                self.rotate_tag = char
                return True
            elif tag == "/rotat":
                self.rotate_tag = None
                return True

            elif tag == "chaos":
                self.chaos_tag = True
                return True
            elif tag == "/chaos":
                self. chaos_tag = False
                return True

            elif tag == "move":
                self.move_tag = True
                return True
            elif tag == "/move":
                self.move_tag = False
                return True

            elif tag == "omega":
                self.omega_tag = char
                return True
            elif tag == "/omega":
                self.omega_tag = None
                return True

            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # I'd never advise having the omega tag alongside other custom tags
            if self.omega_tag is not None:
                new_string += "{" + self.omega_tag + "}"
            if self.bounce_tag is not None:
                new_string += "{" + self.bounce_tag + "}"
            if self.fade_in_tag is not None:
                new_string += "{" + self.fade_in_tag + "}"
            if self.scare_tag is not None:
                new_string += "{" + self.scare_tag + "}"
            if self.rotate_tag is not None:
                new_string += "{" + self.rotate_tag + "}"
            if self.chaos_tag:
                new_string += "{chaos}"
            if self.move_tag:
                new_string += "{move}"
            # User styles should come before other tags
            if self.user_style is not None:
                new_string += "{" + self.user_style + "}"
            if self.bold:
                new_string += "{b}"
            if self.strikethrough:
                new_string += "{s}"
            if self.underline:
                new_string += "{u}"
            if self.italic:
                new_string += "{i}"
            if self.color is not None:
                new_string += "{" + self.color + "}"
            if self.alpha is not None:
                new_string += "{" + self.alpha + "}"
            if self.font is not None:
                new_string += "{" + self.font + "}"

            if self.size is not None:
                new_string += "{" + self.size + "}"
            if self.outline_color is not None:
                new_string += "{" + self.outline_color + "}"
            if self.plain:
                new_string += "{plain}"

            new_string += char

            # You MUST end your custom tags in reverse order!! (Unless they're self-closing)
            if self.move_tag:
                new_string += "{/move}"
            if self.chaos_tag:
                new_string += "{/chaos}"
            if self.rotate_tag is not None:
                new_string += "{/" + self.rotate_tag + "}"
            if self.scare_tag is not None:
                new_string += "{/" + self.scare_tag + "}"
            if self.fade_in_tag is not None:
                new_string += "{/" + self.fade_in_tag + "}"
            if self.bounce_tag is not None:
                new_string += "{/" + self.bounce_tag + "}"

            if self.omega_tag is not None:
                new_string += "{/" + self.omega_tag + "}"

            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""
            if self.omega_tag is not None:
                new_string += "{" + self.omega_tag + "}"
            if self.bounce_tag is not None:
                new_string += "{" + self.bounce_tag + "}"
            if self.fade_in_tag is not None:
                new_string += "{" + self.fade_in_tag + "}"
            if self.scare_tag is not None:
                new_string += "{" + self.scare_tag + "}"
            if self.rotate_tag is not None:
                new_string += "{" + self.rotate_tag + "}"
            if self.chaos_tag:
                new_string += "{chaos}"
            if self.move_tag:
                new_string += "{move}"

            if self.user_style is not None:
                new_string += "{" + self.user_style + "}"
            if self.bold:
                new_string += "{b}"
            if self.strikethrough:
                new_string += "{s}"
            if self.underline:
                new_string += "{u}"
            if self.italic:
                new_string += "{i}"
            if self.color is not None:
                new_string += "{" + self.color + "}"
            if self.alpha is not None:
                new_string += "{" + self.alpha + "}"
            if self.font is not None:
                new_string += "{" + self.font + "}"
            if self.size is not None:
                new_string += "{" + self.size + "}"
            if self.outline_color is not None:
                new_string += "{" + self.outline_color + "}"
            if self.plain:
                new_string += "{plain}"

            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            if self.move_tag:
                new_string += "{/move}"
            if self.chaos_tag:
                new_string += "{/chaos}"
            if self.rotate_tag is not None:
                new_string += "{/" + self.rotate_tag + "}"
            if self.scare_tag is not None:
                new_string += "{/" + self.scare_tag + "}"
            if self.fade_in_tag is not None:
                new_string += "{/" + self.fade_in_tag + "}"
            if self.bounce_tag is not None:
                new_string += "{/" + self.bounce_tag + "}"
            if self.omega_tag is not None:
                new_string += "{/" + self.omega_tag + "}"

            return new_string

    # If you are using the modified text.py, then add these lines to any class you
    # want them to be used on. This will enable the Text holding your Wrapper
    # class so send its style and style prefix updates down to your wrapper
    # which can then update its child. Otherwise you can ignore this completely.
    """
    def set_style_prefix(self, prefix, root):
        super(BounceText, self).set_style_prefix(prefix, root)
        self.child.set_style_prefix(prefix, root)
    def set_style(self, style):
        self.child.set_style(style)
    """

    # Basic text displacement demonstration
    class BounceText(renpy.Displayable):
        def __init__(self, child, char_offset, bounce_height=20, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(BounceText, self).__init__(**kwargs) # REMEMBER TO RENAME HERE TO YOUR CLASS

            # For all of my classes, I assume I am being passed a displayable
            # of class Text. If you might not, I recommend going with the default of
            # self.child = renpy.displayable(child)
            self.child = child

            self.bounce_height = bounce_height # The amplitude of the sine wave
            self.char_offset = char_offset # The offset into the sine wave
            self.freq = 4.0 # How fast the text moves up and down

        def render(self, width, height, st, at):
            # Where the current offset is calculated
            # (self.char_offset * -.1) makes it look like the left side is leading
            # We use st to allow this to change over time
            curr_height = math.sin(self.freq*(st+(float(self.char_offset) * -.1))) * float(self.bounce_height)

            ####  A transform will only alter zoom or alpha as far as I know with Text  ####
            # t = Transform(child=self.child,  alpha = curr_height)

            # Create a render from the child.
            # Replace self.child with t to include an alpha or zoom transform
            child_render = renpy.render(self.child, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # This will position our child's render. Replacing our need for an offset Transform
            render.subpixel_blit(child_render, (0, curr_height))

            renpy.redraw(self, 0) # This lets it know to redraw this indefinitely
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    # Simple fade in. Helps show some ideas for timing
    # May want to modify to allow it to skip to the end if the user clicks.
    # Otherwise plays for the full time given.
    class FadeInText(renpy.Displayable):
        def __init__(self, child, char_num, fade_time, **kwargs):
            super(FadeInText, self).__init__(**kwargs)

            # The child.
            self.child = child
            self.fade_time = fade_time
            self.char_num = char_num
            self.display_time = .01
            self.slide_distance = 100
            # This is to get seconds per character on screen for later
            # Allowing this effect to scale with the player's desired text speed
            self.cps = 0.0
            if renpy.game.preferences.text_cps is not 0: # Avoid division by 0.0
                self.cps = (1.0 / renpy.game.preferences.text_cps)

        def render(self, width, height, st, at):
            # How long to wait before doing things
            time_offset = self.char_num * self.cps
            alpha_time = 0.0
            xoff = 5.0
            if st > time_offset:
                adjust_st = st - time_offset # Adjust for time delay
                alpha_time = adjust_st/self.fade_time
                xoff = self.slide_distance - ((adjust_st/self.fade_time) * self.slide_distance)
                if xoff < 0:
                    xoff = 0
            # Example of using transform to adjust alpha
            t = Transform(child=self.child,  alpha = alpha_time)
            child_render = renpy.render(t, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (xoff, 0))

            if st <= self.fade_time + time_offset:
                renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Simple random motion effect
    class ScareText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ScareText, self).__init__(**kwargs)

            self.child = child

            self.square = square # The size of the square it will wobble within.
            # Include more variables if you'd like to have more control over the positioning.

        def render(self, width, height, st, at):
            # Randomly move the offset of the text's render.
            xoff = (renpy.random.random()-.5) * float(self.square)
            yoff = (renpy.random.random()-.5) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    # Demonstration of changing text styles on the fly
    # Could also predefine some styles and swap between those as well!
    # Also for this effect in particular, I ---HIGHLY--- advise building in some way to disable it
    # as it can be pretty harsh on the eyes.
    # An example of how you can make this a preference option is included below.
    class ChaosText(renpy.Displayable):
        # Some may want to have this list be more of a global variable than baked into the class.
        font_list = ["FOT-PopJoyStd-B.otf", "GrenzeGotisch-VariableFont_wght.ttf", "Pacifico-Regular.ttf", "RobotoSlab-ExtraBold.ttf",\
                     "RobotoSlab-Medium.ttf", "SyneTactile-Regular.ttf", "TurretRoad-Bold.ttf", "TurretRoad-ExtraBold.ttf", "TurretRoad-ExtraLight.ttf", \
                     "TurretRoad-Light.ttf", "TurretRoad-Medium.ttf", "TurretRoad-Regular.ttf"]
        #Just a list so we can pull any hex value randomly
        color_choice = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        def __init__(self, orig_text, **kwargs):

            super(ChaosText, self).__init__(**kwargs) #REMEMBER TO RENAME HERE TO YOUR CLASS

            # Create our child
            self.child = renpy.text.text.Text(orig_text)
            self.orig_text = orig_text
            self.last_style = None # This will be used for renders if the user wants to stop chaos text

        def render(self, width, height, st, at):
            if not gui.chaos_on:                # This preference is defined near the top of this file.  And can be set in the preferences screen (see line 783-787 in screens.rpy)
                if self.last_style is not None: # If this is our first render, then should do that first
                    # Rest of this is just a repeat of what's below.
                    self.child.set_text(self.last_style.apply_style(self.orig_text))
                    child_render = renpy.render(self.child, width, height, st, at)
                    self.width, self.height = child_render.get_size()
                    render = renpy.Render(self.width, self.height)
                    render.subpixel_blit(child_render, (0, 0))
                    return render

            # We'll create a new text style for this render
            new_style = DispTextStyle()
            new_color = ""
            # Create a random color using hex values
            for i in range(0,6):
                new_color += renpy.random.choice(self.color_choice)
            new_color = "#" + new_color
            new_style.add_tags("color=" + str(new_color))
            # Random size
            rand_size = renpy.random.randint(0,50)
            new_style.add_tags("size="+str(rand_size))
            # Random font
            rand_font = renpy.random.choice(self.font_list)
            new_style.add_tags("font="+rand_font)
            #Apply our style to our Text child
            self.child.set_text(new_style.apply_style(self.orig_text))
            # Create a render from the child.
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self,0)

            self.last_style = new_style # Save the current style for if the user wishes to turn off the Chaos tag
            return render

        def visit(self):
            return [ self.child ]

    # Could honestly still use some work. But it's a start and good proof of concept
    # Credit to the FancyText module creator yukinogatari for the idea.
    # FancyText module can be found at https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=59587
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=100, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child

            self.speed = speed # The speed of our rotation

        def render(self, width, height, st, at):

            theta = math.radians(st * float(self.speed))
            c, s = math.cos(theta), math.sin(theta)

            child_render = renpy.render(self.child, width, height, st, at)

            child_render.reverse = renpy.display.matrix.Matrix2D(c, -s, s, c)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            # Try to adjust the positioning with the rotataion. Honestly needs more work
            # I just didn't feel like doing the math for it right now.
            render.subpixel_blit(child_render, (s * self.width+5, -c * self.height/2 + 10))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    """
    # Example of above but using matrix functions. Some may find it more useful.
    class RotateText(renpy.Displayable):
        def __init__(self, child, speed=100, **kwargs):
            super(RotateText, self).__init__(**kwargs)

            self.child = child

            self.speed = speed # The speed of our rotation

        def render(self, width, height, st, at):
            # Altering this can allow you to rotate in the x and y axis as well!!
            # They're honestly probably easier to make look good too...
            rotation_m = renpy.display.matrix.rotate(0,st*self.speed,0)

            child_render = renpy.render(self.child, width, height, st, at)
            c_width, c_height = child_render.get_size()

            child_render.reverse = rotation_m

            # Math nerds might realize I'm not offsetting the transform.
            # While renpy.display.matrix.offset(x,y,z) would seem to do that
            # In my experiments it didn't do much to help. Feel free to play around
            # with it though if you want. Other matrix functions include
            # renpy.display.matrix.perspective(w,h,n,p,f)
            # renpy.display.matrix.screen_projection(w,h) < Renpy space to OpenGL viewport
            # renpy.display.matrix.texture_projection(w,h) < Renpy space to OpenGL render-to-texture
            # You can look up more about them in the renpy\display\matrix_functions.pyx file

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            xoff = 0
            #Rotations on y axis
            theta = math.radians(st * float(self.speed))
            s = math.cos(theta)
            xoff= (-s * self.width/2) + 3 # +3 just to give some space from other letters.

            yoff = 0
            #Rotations on x axis
            #theta2 = math.radians(st * float(self.speed) + 180)
            #c = math.cos(theta2) + 1.0
            #yoff = c * self.height
            #if yoff > self.height:
            #    yoff = self.height

            # Try to adjust the positioning with the rotataion. Honestly needs more work
            # I just didn't feel like doing the math for it right now.

            render.subpixel_blit(child_render, (xoff,yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]
    """

    # Simple text swap effect
    # It can be prone to having letters out of place when part of a larger string
    # I recommended you pass it the entire line to avoid this issue.
    # Can also just define every line it'll need in advance and just tell it which
    # ones to swap to to be extra sneaky. Then the text won't be in your script at all!
    class SwapText(renpy.Displayable):
        def __init__(self, start_tags, text1, text2, end_tags, swap_time, **kwargs):
            super(SwapText, self).__init__(**kwargs)
            #Style tags we'll need as well as the text
            self.start_tags = start_tags
            self.text1 = text1
            self.text2 = text2
            self.end_tags = end_tags
            # How long between swapping text
            self.s_time = swap_time
            # An internal timer to keep track of when to swap
            self.timer = 0.0
            # Determines if we swap to text1 or text2 next
            self.swap_to_1 = False
            self.child = Text(start_tags + text1 + end_tags)
            self.st = 0.0


        def render(self, width, height, st, at):
            delta = st - self.st # How long since last update
            self.timer += delta
            if self.timer > self.s_time:
                # If time to swap, determine which one to swap to.
                if self.swap_to_1:
                    self.child.set_text(self.start_tags + self.text1 + self.end_tags)
                    self.swap_to_1 = False
                    self.timer = 0.0
                else:
                    self.child.set_text(self.start_tags + self.text2 + self.end_tags)
                    self.swap_to_1 = True
                    self.timer = 0.0

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0,0))
            renpy.redraw(self, 0)

            self.st = st # So we can check how long since last update
            return render

        def visit(self):
            return [ self.child ]

    # An example of text that moves and reacts to the mouse.
    class MoveText(renpy.Displayable):
        def __init__(self, child, **kwargs):
            super(MoveText, self).__init__(**kwargs)

            self.child = child
            self.xpos = 0.0
            self.ypos = 0.0

        def render(self, width, height, st, at):
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            # Use our child's position as determined by the event function
            render.subpixel_blit(child_render, (self.xpos, self.ypos))
            return render

        # Mostly stolen from the SpriteManager example in the documentation
        def event(self, ev, x, y, st):
            # x and y are relative to the top left corner of the displayable initially.
            # So we'll want to update it to reflect the actual position of our text
            trans_x = x - self.xpos - (self.width / 2)
            trans_y = y - self.ypos - (self.height / 2)
            distance = math.hypot(trans_x , trans_y )

            vl = math.hypot(trans_x,trans_y)
            if vl >= 150:
                return
            distance = 3.0 * (150-vl) / 150
            self.xpos -= distance * trans_x / vl
            self.ypos -= distance * trans_y / vl
            renpy.redraw(self, 0)

            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

    # Our Custom Tag Functions
    def bounce_tag(tag, argument, contents):
        new_list = [ ] # The list we will be appending our displayables into
        if argument == "": # If the argument received is blank, insert a default value
            argument = 10
        char_offset = 0  # Since we want our text to move in a wave,
                         # we want to let each character know where it is in the wave.
                         # So they move in harmony. Otherwise they rise and fall all together.
        my_style = DispTextStyle() # This will keep track of what tags and styling to add to each letter
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:                                            # Extract every character from the string
                    char_text = Text(my_style.apply_style(char))             # Create a Text displayable with our styles applied
                    char_disp = BounceText(char_text, char_offset, argument) # Put the Text into the Wrapper
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))     # Add it back in as a displayable
                    char_offset += 1
            elif kind == renpy.TEXT_TAG:
                # Filter for every kind of tag we accept
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            # I honestly never got around to testing this. Not often the text
            # already has a displayable in it. Let me know if it breaks though.
            elif kind == renpy.TEXT_DISPLAYABLE:
                char_disp = BounceText(text, char_offset, argument)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                char_offset += 1
            else: # Don't touch any other type of content
                new_list.append((kind,text))

        return new_list

    def fade_in_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            my_index = 0
            fade_time = 5.0
        else: # Note: if you include one argument, you should include both
            my_index_str, _, fade_time_str = argument.partition('-')
            # my_index is meant to be how far into the string the letter is
            # that way it can schedule when to move based on the first character
            # to be displayed
            my_index = int(my_index_str)
            fade_time = float(fade_time_str)
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' ')) # Skips blank space since looks weird counting it
                        continue
                    char_text = Text(my_style.apply_style(char))
                    char_disp = FadeInText(char_text, my_index, fade_time)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    def scare_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    def chaos_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_disp = ChaosText(my_style.apply_style(char))
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    def rotate_tag(tag, argument, contents):
        new_list = [ ]
        # Argument here will reprsent the desired speed of the rotation.
        if argument == "":
            argument = 100
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = RotateText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    def swap_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return contents
        # This tag expects that each argument is the same length and that it is
        # applied to a length of text of equal length to the arguments.
        # This is a pretty static way of doing it mostly made to demonstrate the concept.
        # You'll probably want to allow yours more flexibility depending on your needs.
        text1, _, argument = argument.partition("@")
        text2, _, argument = argument.partition("@")
        if len(text1) != len(text2):
            new_list.append((renpy.TEXT_TEXT, "ERROR!"))
        swap_time = float(argument)

        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                # This one replaces the whole text rather than extracting over letters
                # That way it can take up this whole block with its own Text displayable
                char_disp = SwapText(my_style.start_tags(), text1, text2, my_style.end_tags(), swap_time)
                new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    def move_tag(tag, argument, contents):
        new_list = [ ]
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = MoveText(char_text)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # Turns out some text effects won't allow for a paragraph break if applied to a whole line
    # Which can cause your text to just continue straight off the screen.
    # To amend this, you can insert the {para} tag.
    # This will let the Text displayable holding us know when to wrap.
    def paragraph_tag(tag, argument):
        return [(renpy.TEXT_PARAGRAPH, "")]

    # This tag is made to automatically wrap several Classes inside one another
    # This is to reduce strain on the render pipeline and memory from nested classes
    # SwapText is not included in this due to it replacing whole sections rather than
    # individual letters. Would be better to embed an Omega inside a SwapText.
    # MoveText as been omitted as well due to the others applying various transforms
    # Would be better to have an event call attached to one of those so it keep track
    # of the position more easily.
    def omega_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "": # This tag must have arguments
            return contents
        # Variable for each of our tags. None if it takes one argument.
        # Boolean if 0 or many arguments.
        bt_tag = None
        sc_tag = None
        fi_tag = False
        rot_tag = None
        chao_tag = False
        fi_arg_1 = None
        fi_arg_2 = None

        args = [ ]
        arg_count = argument.count('@') # Count how many partitions we will need to make
        for x in range(arg_count):      # Extract all the tags and arguments with them
            new_arg, _, argument = argument.partition('@')
            args.append(new_arg)
        args.append(argument)
        # Determine what tags we'll need to apply and the arguments associated with them
        for arg in args:
            tag, _, value = arg.partition('=')
            if tag == "BT":
                if value is not "":
                    bt_tag = value
                else:
                    bt_tag = 10
            elif tag == "SC":
                if value is not "":
                    bt_tag = value
                else:
                    bt_tag = 5
            # Multiargument tag example. Be sure to use different partitions for these
            elif tag == "FI":
                fi_tag = True
                str1, _, str2 = value.partition('-')
                fi_arg_1 = int(str1)
                fi_arg_2 = float(str2)
            elif tag == "ROT":
                rot_tag = value
            elif tag == "CH":
                chao_tag = True

        my_style = DispTextStyle()
        my_index = 0 # Some Classes will need an index
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    # Apply base Wrappers to letter
                    if chao_tag:
                        char_disp = ChaosText(my_style.apply_style(char))
                    else:
                        char_disp = Text(my_style.apply_style(char))
                    # Apply further Wraps
                        # Be sure to consider if the order will be important to you
                    if bt_tag is not None:
                        char_disp = BounceText(char_disp, my_index, bt_tag)
                    if sc_tag is not None:
                        char_disp = ScareText(char_disp, sc_tag)
                    if fi_tag:
                        char_disp = FadeInText(char_disp, my_index + fi_arg_1, fi_arg_2)
                    if rot_tag is not None:
                        char_disp = RotateText(char_disp, rot_tag)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list

    """

    # Template tag function to copy off of.
    def TEMPLATE_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = TEMPLATEText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
         return new_list
    """

    # Define our new text tags
    config.custom_text_tags["bt"] = bounce_tag
    config.custom_text_tags["fi"] = fade_in_tag
    config.custom_text_tags["sc"] = scare_tag
    config.custom_text_tags["rotat"] = rotate_tag
    config.custom_text_tags["chaos"] = chaos_tag
    config.custom_text_tags["swap"] = swap_tag
    config.custom_text_tags["move"] = move_tag
    config.custom_text_tags["omega"] = omega_tag
    config.self_closing_custom_text_tags["para"] = paragraph_tag
    # Template tag function
    #config.custom_text_tags[""] = _tag

    ##### Made these ones just for fun. Leaving them in here just in case anyone wants
    ##### to use them. Probably will not add them to the Omega tag or to DispTextStyle

    # Determines what color to apply to a letter in the gradient and gradient2 tags
    def color_gradient(color_1, color_2, range, index):
        """
        'color_1'
            String representing a color in hex. Format being rrggbb. Considered the start of the gradient
        'color_2'
            Same as above. Considered the end of the gradient
        'range'
            The number elements in the gradient
        'id'
            The id into the gradient

        returns a string representing the index into the gradient
        """
        rv = "#" # rv stands for return value
        # Return early if at the ends
        if index == 0:
            return color_1
        if range == index:
            return color_2
        # Helps with conversion from string to int through hex
        def str_to_int(str):
            return int("0x" + str, base=16)
        # Decompose the strings into rgb parts
        red_1 = str_to_int(color_1[1:3])
        red_2 = str_to_int(color_2[1:3])
        green_1 = str_to_int(color_1[3:5])
        green_2 = str_to_int(color_2[3:5])
        blue_1 = str_to_int(color_1[5:7])
        blue_2 = str_to_int(color_2[5:7])

        # Get value of color
        red_f = red_1 + (index * (red_2 - red_1) / range)
        green_f = green_1 + (index * (green_2 - green_1) / range)
        blue_f = blue_1 + (index * (blue_2 - blue_1) / range)

        # If a value is over 255, then you input something wrong
        if red_f > 255 or green_f > 255 or blue_f > 255:
            renpy.notify("ERROR IN COLOR_GRADIENT")
        # Get the hex value of the rgb channels
        hex_red = hex(red_f)   # Convert to a hex string
        hex_red = hex_red[2:4] # Strip the leading "0x"
        hex_green = hex(green_f)
        hex_green = hex_green[2:4]
        hex_blue = hex(blue_f)
        hex_blue = hex_blue[2:4]
        # Append a 0 to the string if we'd only get one character
        if red_f < 16:
            hex_red = "0" + hex_red
        if green_f < 16:
            hex_green = "0" + hex_green
        if blue_f < 16:
            hex_blue = "0" + hex_blue
        rv = rv + hex_red + hex_green + hex_blue
        return rv

    # This tag applies a static gradient over text
    def gradient_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: # Note: all arguments must be supplied
            col_1, _, col_2 = argument.partition('-')
        # Get a count of all the letters we will be applying colors to
        count = 0
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        continue
                    count += 1
        count -= 1
        my_index = 0
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    new_list.append((renpy.TEXT_TAG, "color=" + color_gradient(col_1, col_2, count, my_index)))
                    new_list.append((renpy.TEXT_TEXT, char))
                    new_list.append((renpy.TEXT_TAG, "/color"))
                    my_index += 1
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    # A custom displayable that applies a gradient over a letter of text.
    # Honestly didn't test this works with other text tags since was just for fun
    class GradientText(renpy.Displayable):
        def __init__(self, char, col_list, id, list_end, **kwargs):
            """
            col_list format
                (color_1, color_2, end_id)
            list_end should be the number of gradients in the list
            """
            super(GradientText, self).__init__(**kwargs)

            self.char = char
            self.child = Text(char)
            self.col_list = col_list # Calling it grad_list for gradient might be more appropriate.
            self.id = id
            self.list_end = list_end
            # Figure out which gradient we are in
            for i, element in enumerate(col_list):
                if self.id < element[2]:
                    self.curr_grad = i
                    break
            # Determine the current range (for color_gradient func later)
            if self.curr_grad is 0:
                self.curr_range = self.col_list[0][2]
            else:
                self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

        def render(self, width, height, st, at):
            my_style = DispTextStyle()
            # Get the color to apply to the text
            if self.curr_grad == 0:
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id))
            else: # color_gradient() expects id to be within the range given. So must reduce to that if exceeding it.
                my_style.add_tags("color=" + color_gradient(self.col_list[self.curr_grad][0], self.col_list[self.curr_grad][1], self.curr_range, self.id - self.col_list[self.curr_grad - 1][2]))

            # Usual retrieval and drawing of child render
            self.child.set_text(my_style.apply_style(self.char))
            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (0, 0))
            renpy.redraw(self, 0)

            # Iterate id for next render
            self.id += 1
            # If we are at the end of the range update gradient
            if self.id > self.col_list[self.curr_grad][2]:
                self.curr_grad += 1
                # If at the end of our color list, reset back to 0
                if self.curr_grad == self.list_end:
                    self.curr_grad = 0
                    self.id = 0
                    self.curr_range = self.col_list[0][2]
                # Otherwise just update the range
                else:
                    self.curr_range = self.col_list[self.curr_grad][2] - self.col_list[self.curr_grad - 1][2]

            return render

        def visit(self):
            return [ self.child ]

    # This tag applies a gradient that smoothly rolls over the letters
    def gradient2_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            return
        else: # Note: All arguments must be supplied
            arg_num, _, argument = argument.partition('-') # Number of gradients to read
        arg_num = int(arg_num)
        # Get all arguments
        col_list = []
        for i in range(arg_num):
            col_1, _, argument = argument.partition('-')   # Color 1
            col_2, _, argument = argument.partition('-')   # Color 2
            end_num, _, argument = argument.partition('-') # Last index of the gradient
            col_list.append((col_1, col_2, int(end_num)))

        my_index = 0
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if char == ' ':
                        new_list.append((renpy.TEXT_TEXT, ' '))
                        continue
                    char_disp = GradientText(my_style.apply_style(char), col_list, my_index, arg_num)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
                    my_index += 1
                    # Wrap around if reached the end of the gradient list.
                    if my_index >= col_list[arg_num-1][2]:
                        my_index = 0
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["gradient"] = gradient_tag
    config.custom_text_tags["gradient2"] = gradient2_tag
