import streamlit as st

class MultiPage:
    def __init__(self):
        self.apps = []
        self.app_names = []
        self.default = ''

    def add_app(self, title, func, args=None):
        self.app_names.append(title)
        self.apps.append({
            "title": title,
            "function": func,
            "args":args
        })

    def run(self):
        # get query_params
        query_params = st.experimental_get_query_params()
        self.default = query_params["app"][0] if "app" in query_params else None
        default_index = self.app_names.index(self.default) if self.default else 0
        # simple radio button for navigation
        app = st.sidebar.radio(
            'Go To',
            self.apps,
            index = default_index,
            format_func=lambda app: app['title'],
            key = 'Navigation')
        # reflect the current app in query_params
        self.default = app['title']
        st.experimental_set_query_params(app=self.default)
        # runs the selected app with passes args
        app['function'](app['args'])