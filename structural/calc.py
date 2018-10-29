import report
import util

class BaseCalc(object):

    def __init__(self, title="", project="", project_number="", by=""):
        self.title = title
        self.project = project
        self.project_number = project_number
        self.by = by

    def __unicode__(self):
        if not isinstance(self.project, str):
            return u"%s" % self.name
        if self.project and self.project_number and self.title:
            return u"%s - %s - %s" % (self.project_number, self.project, self.title)
        elif self.project and self.title:
            return u"%s - %s" % (self.project, self.title)
        elif self.project_number and self.title:
            return u"Project %s - %s" % (self.project_number, self.title)
        elif self.project and self.project_number:
            return u"%s - %s" % (self.project_number, self.project)
        elif self.project:
            return u"%s" % (self.project)
        elif self.project_number:
            return u"%s" % (self.project_number)
        elif self.title:
            return u"%s" % (self.title)
        else:
            return u""

    def timestamp(self):
        return util.timestamp()

    def init_components(self):
        "Initialize component instances to be overridden by child class"
        raise NotImplementedError

    def render(self, template_type="txt"):
        return report.Report(self).render(template_type)

    def recalc(self):
        "Perform the calculations needed to produce results"
        # Implement in derived class
        raise NotImplementedError, "Derived class does not implement recalc()"

