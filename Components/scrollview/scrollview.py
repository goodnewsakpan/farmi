from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from kivy.properties import OptionProperty, BooleanProperty, ObjectProperty, NumericProperty, ListProperty
from kivy.animation import Animation
from kivymd.uix.behaviors import StencilBehavior

from Components.effects import LowerScrollEffect, LowerDampedScrollEffect

__all__ = ("LEFT", "RIGHT", "DOWN", "UP", "NULL", "RealRecycleView")

LEFT = 1  # finger and content moves right (scroll bar moves left) to see the far left of the entire content
RIGHT = 2  # finger and content moves left (scroll bar moves right) to see the far right of the entire content
DOWN = 3  # finger and content moves up (scroll bar moves down) to see the very bottom of the entire content
UP = 4  # finger and content moves down (scroll bar moves up) to see the very top of the entire content
NULL = 0  # finger or scroll bar or content is not moving


