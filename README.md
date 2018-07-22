# Description
Needed to start a Bokeh dashboard programmatically and have the possibility to; 

1. Code reuse in the dashboard, use code from other modules in the project   
2. Attach custom jinja2 template 
3. Attach Custom static directory 

 
When using the standard directory structure, it’s not possible to use code from other modules outside the Bokeh directory structure.  

Created a CustomHandler that mixes function handler with Directory handel. 

 
## Note: 
When using the command ‘bokeh serve <name>’  the server adds the Bokeh static directory before adding the custom static directory. In the current state this does not work. The Bokeh css and js files need to placed in the custom static directory 

## base
Base module holds a Bokeh example from their github repo
https://github.com/bokeh/bokeh/tree/master/examples/app/dash
