#!/usr/bin/env python3

import os.path
from abc import ABCMeta, abstractmethod
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets, QtGui

# This is the location of the "*.ui" files. These are in the directory "ui_forms" which is assumed
# to be in the same directory as this file. If either this file changes location or the location of
# "*.ui" files changes, this constant should be updated.
SOURCE_LOCATION = os.path.join(os.path.dirname(__file__), "ui_forms/")

class QtABCMeta(QtCore.pyqtWrapperType, ABCMeta):
    """This class is to stop metaclass conflicts.

    These conflicts happen when trying to create an abstract base class that is derived by a class
    which derives one of PyQt's types. See the following web page for more information:
    https://stackoverflow.com/a/28727066
    """

    pass

class DatabaseResourceForm(QtWidgets.QWidget, metaclass = QtABCMeta):
    """This class is designed to be the base class of the widgets used in the tab widget of the
    main application window.

    This class has functionality to allow the form to respond to a database change or a resource
    root change. The two methods which handle this have default implementations. However, a model
    reset is needed when the database or resource root changes; the method which handles this is
    abstract and therefore must be implemented by the child class. This is done so that the form
    can re-instantiate the model it needs to use.

    Attributes:
        database: This is the current database in use by this form.
        resource_root: This is the current resource root in use by this form.
        model: This is the current model in use by this form.
    """

    def __init__(self, parent = None):
        super().__init__(parent)
        self.database = None
        self.resource_root = None
        self.model = None

    def set_database(self, database):
        """Set a new database to interact with."""
        self.database = database
        self.reset_model()

    def set_resource_root(self, resource_root):
        """Set a new resource root to use internally."""
        self.resource_root = resource_root
        self.reset_model()

    @abstractmethod
    def reset_model(self):
        """Adapts the form to a change of model or resource root."""
        pass

def resource_icon(model, index, resource_root = None):
    # The filename of the icon we are to load should be the same data in the database
    # itself. We can extract this information from the model by using the very function
    # we are in; just by modifying the intended role but maintaining the index.
    stored_filename = model.data(index, Qt.EditRole)
    if not stored_filename:
        return None

    # We can try three different methods to find the file to load. The first method is to
    # prepend the resource root (the primary use of this variable). The second is to load
    # the file with the filename, as is. The last is to prepend "./". We do not consider
    # the first method if the resource root variable is invalid.
    icon_filenames = [
        stored_filename,
        os.path.join("./", stored_filename),
    ]
    if resource_root:
        icon_filenames.insert(0, os.path.join(resource_root, stored_filename))

    # Check the validity of the filenames be checking to see if the file exits.
    valid_icon_filenames = list(filter(os.path.exists, icon_filenames))
    if len(valid_icon_filenames) == 0:
        return None
    icon_filename = valid_icon_filenames[0]
    return QtGui.QIcon(icon_filename)