from pyramid_debugtoolbar.panels import DebugPanel

_ = lambda x: x

class RequestVarsDebugPanel(DebugPanel):
    """
    A panel to display request variables (POST/GET, session, cookies).
    """
    name = 'RequestVars'
    has_content = True

    def nav_title(self):
        return _('Request Vars')

    def title(self):
        return _('Request Vars')

    def url(self):
        return ''

    def content(self):
        vars = {}
        vars.update({
            'get': [(k, self.request.GET.getall(k)) for k in self.request.GET],
            'post': [(k, self.request.POST.getall(k)) for k in
                     self.request.POST],
            'cookies': [(k, self.request.cookies.get(k)) for k in
                        self.request.cookies],
            'view_name': '%s' % self.request.view_name,
        })
        if hasattr(self.request, 'session'):
            vars.update({
                'session': [(k, self.request.session.get(k)) for k in
                            self.request.session.keys()]
            })

        return self.render(
            'pyramid_debugtoolbar.panels:templates/request_vars.jinja2',
            vars,
            request=self.request)

