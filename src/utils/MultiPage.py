import streamlit as st

class MultiPage:
    def __init__(self):
        self.apps = []
        self.app_names = []

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
        choice = query_params["app"][0] if "app" in query_params else None
        # common key
        key='Navigation'
        # on_change callback
        def on_change():
            params = st.experimental_get_query_params()
            params['app'] = st.session_state[key]
            st.experimental_set_query_params(**params)
        # update session state
        st.session_state[key] = choice if choice in self.app_names else self.app_names[0]
        appname = st.sidebar.radio('Go To', self.app_names, on_change=on_change, key=key)
        # run the selected app
        for app in self.apps:
            if app['title'] == appname:
                app['function'](app['args'])