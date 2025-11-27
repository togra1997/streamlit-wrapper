from dataclasses import dataclass

import streamlit as st

from .base import StreamBase
from .wigets import Label, Wiget


@dataclass
class Col(StreamBase):
    def set_wiget(self):
        col = st.columns(2)
        with col[0]:
            data = Wiget("col1").data
            Label(data)

        with col[1]:
            data = Wiget("col2").data
            Label(data)
