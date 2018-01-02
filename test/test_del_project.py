import random
import string

from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_del_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    name = random_string("test_", 10)
    description = random_string("description ", 10)
    if app.project.get_list() == 0:
        app.project.add(Project(name=name, description=description))
    old_projects = app.project.get_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    app.session.logout()
