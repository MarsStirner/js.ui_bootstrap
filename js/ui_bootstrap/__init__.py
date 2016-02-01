from fanstatic import Library
from fanstatic import Resource
from js.angular import angular
from js.bootstrap import bootstrap

library = Library('fancybox', 'resources')

ui_bootstrap = Resource(
    library, 'ui-bootstrap-tpls-1.1.1.js',
    minified='ui-bootstrap-tpls-1.1.1.min.js',
    depends=[angular, bootstrap]
)
ui_bootstrap_no_templates = Resource(
    library, 'ui-bootstrap-1.1.1.js',
    minified='ui-bootstrap-1.1.1.min.js',
    depends=[angular, bootstrap]
)
