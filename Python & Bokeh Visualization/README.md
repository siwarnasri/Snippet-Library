# Data Visualization in Python With Bokeh

Bokeh prides itself on being a library for interactive data visualization.

Unlike popular counterparts in the Python visualization space, like Matplotlib and Seaborn, Bokeh renders its graphics using HTML and JavaScript. This makes it a great candidate for building web-based dashboards and applications. However, it’s an equally powerful tool for exploring and understanding your data or creating beautiful custom charts for a project or report.

### From Data to Visualization: 

Building a visualization with Bokeh involves the following steps:

>Prepare the data
>Determine where the visualization will be rendered
>Set up the figure(s)
>Connect to and draw your data
>Organize the layout
>Preview and save your beautiful data creation

### Preview and Save Your Beautiful Data Creation:

Whether you’re viewing your visualization in a browser or notebook, you’ll be able to explore your visualization, examine your customizations, and play with any interactions that were added.

If you like what you see, you can save your visualization to an image file. Otherwise, you can revisit the steps above as needed to bring your data vision to reality.

### Generating Your First Figure:

There are multiple ways to output your visualization in Bokeh:

> output_file('filename.html') will write the visualization to a static HTML file.
> output_notebook() will render your visualization directly in a Jupyter Notebook.

It’s important to note that neither function will actually show you the visualization. That doesn’t happen until show() is called. However, they will ensure that, when show() is called, the visualization appears where you intend it to.

By calling both output_file() and output_notebook() in the same execution, the visualization will be rendered both to a static HTML file and inline in the notebook. However, if for whatever reason you run multiple output_file() commands in the same execution, only the last one will be used for rendering.

### Getting Your Figure Ready for Data:

Now that you know how to create and view a generic Bokeh figure either in a browser or Jupyter Notebook, it’s time to learn more about how to configure the figure() object.

The figure() object is not only the foundation of your data visualization but also the object that unlocks all of Bokeh’s available tools for visualizing data. The Bokeh figure is a subclass of the Bokeh Plot object, which provides many of the parameters that make it possible to configure the aesthetic elements of your figure.

There is tons more I could touch on here, but don’t feel like you’re missing out. Here are some other helpful links on the topic:

The Bokeh Plot Class is the superclass of the figure() object, from which figures inherit a lot of their attributes.
The Figure Class documentation is a good place to find more detail about the arguments of the figure() object.
Here are a few specific customization options worth checking out:

Text Properties covers all the attributes related to changing font styles, sizes, colors, and so forth.
TickFormatters are built-in objects specifically for formatting your axes using Python-like string formatting syntax.
Sometimes, it isn’t clear how your figure needs to be customized until it actually has some data visualized in it, so next you’ll learn how to make that happen.

### Drawing Data With Glyphs:

A glyph is a vectorized graphical shape or marker that is used to represent your data, like a circle or square. More examples can be found in the Bokeh gallery. After you create your figure, you are given access to a bevy of configurable glyph methods.
