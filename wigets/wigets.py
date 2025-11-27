from dataclasses import dataclass

import streamlit as st

from .base import StreamBase


@dataclass
class HelloStream(StreamBase):
    greet: str

    def set_wiget(self):
        st.write(f"Hello {self.greet}")


@dataclass
class Inputs(StreamBase):
    key: str
    data: int = None

    def set_wiget(self):
        self.data = st.number_input("Enter a number", value=0, key=self.key)


@dataclass
class Wiget(StreamBase):
    key: str
    data: int = None

    def set_wiget(self):
        HelloStream("World")
        self.data = Inputs(key=self.key).data
        HelloStream("Hellwwwwwww")


@dataclass
class Label(StreamBase):
    text: int = 0

    def set_wiget(self):
        st.write(f"Label: {self.text}")
