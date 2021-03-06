import jinja2.ext

from ..templatetags.webpack_loader import render_bundle, render_entrypoint


class WebpackExtension(jinja2.ext.Extension):
    def __init__(self, environment):
        super(WebpackExtension, self).__init__(environment)
        environment.globals["render_bundle"] = lambda *a, **k: jinja2.Markup(render_bundle(*a, **k))
        environment.globals["render_entrypoint"] = lambda *a, **k: jinja2.Markup(render_entrypoint(*a, **k))
