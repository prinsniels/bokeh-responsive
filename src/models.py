
#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
from os.path import basename, exists, dirname

# External imports
from jinja2 import Environment, FileSystemLoader

# Bokeh imports
from bokeh.util.callback_manager import _check_callback
from bokeh.application.handlers.handler import Handler
#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

class CustomHandler(Handler):
    ''' 
        Handler that can combines Functionhandler functionality with
        the abbility to set custom static files and templates location

        Copied the handler temaplate and added code,
        class should get;
            callback_function: function that modifies the doc
            static_path: path to static dir, must end with static (example ~/static)
            template_path: path to jinja2 remaplate, should be a .html 
    '''

    def __init__(self, *args, **kwargs):
        
        super(CustomHandler, self).__init__(*args, **kwargs)

        if 'callback_function' not in kwargs:
            raise ValueError('Must pass a callback_function to CustomHandler')

        func = kwargs['callback_function']
        _check_callback(func, ('doc',))

        print(kwargs)
        # the function that needs to be excecuted to create the document
        self._func = func
        self._safe_to_fork = True

        # setup the template
        self._template = None

        template_path = kwargs.get('template_path', None)
        if template_path and exists(template_path):
            env = Environment(loader=FileSystemLoader(dirname(template_path)))
            self._template = env.get_template(basename(template_path))

        # Setup static
        self._static = None
        
        static_path = kwargs.get('static_path', None)
        if static_path and exists(static_path):
            self._static = static_path
       
        print(self._static)
        print(self._template)

    # Properties --------------------------------------------------------------

    @property
    def error(self):
        ''' If the handler fails, may contain a related error message.

        '''
        return self._error

    @property
    def error_detail(self):
        ''' If the handler fails, may contain a traceback or other details.

        '''
        return self._error_detail

    @property
    def failed(self):
        ''' ``True`` if the handler failed to modify the doc

        '''
        return self._failed

    # Public methods ----------------------------------------------------------

    def modify_document(self, doc):
        ''' Modify an application document in a specified manner.

        When a Bokeh server session is initiated, the Bokeh server asks the
        Application for a new Document to service the session. To do this,
        the Application first creates a new empty Document, then it passes
        this Document to the ``modify_document`` method of each of its
        handlers. When all handlers have updated the Document, it is used to
        service the user session.

        *Subclasses must implement this method*

        Args:
            doc (Document) : A Bokeh Document to update in-place

        Returns:
            Document

        '''
        ''' 
            Execute the configured ``func`` to modify the document.

            After this method is first executed, ``safe_to_fork`` will return
            ``False``.

        '''
        self._func(doc)

        # change the doc template to the custom doc template
        if self._template is not None:
            doc.template = self._template

        self._safe_to_fork = True


    def static_path(self):
        ''' Return a path to app-specific static resources, if applicable.

        '''
        if self.failed:
            return None
        else:
            return self._static

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
