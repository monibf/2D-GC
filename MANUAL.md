# User Manual

## Installation

See the [README](README.md)

## Importing/Opening

When starting the program the first thing to do is to either import data, or open a previously saved project.

## Importing

It is possible to import data from a text file.
To do this click on `File -> Import data` in the menu bar.
`Ctrl+I` can be used as a shortcut for this (or `Cmd+I` on a mac. This also applies to the other shortcuts).

The file to be opened must consist of lines of comma separated numbers, with a comma at the end of the line too.
All lines must have the same amount of numbers.

## Opening

It is also possible to open a previously saved project.
To do this, select `File -> Open` in the menu bar, or use the shortcut `Ctrl+O`.
This will open a previously saved project.

It is also possible to only save the integration areas or only save the preferences.
When opening a file that only has those, those integration areas or preferences will be applied to the current project.

## Saving

### Saving the project

When there is at least some data, the file can be saved as a project.
Saving the file can be done with `File -> Save` or `File -> Save as` in the menu bar.

When saving for the first time or when choosing `Save as` a file dialog will be opened.
Saved projects should have the extension `.gcgc`.

### Saving the preferences

When choosing `File -> Save preferences` only the preferences will get saved.


### Saving the integration areas

When choosing `File -> Save integration areas` only the integration areas will get saved.

## Exporting
It is possible to export the current 2D or 3D graph as a .png file, this can be done by using either `File -> Export 2D plot` with shortcut `Ctrl + R` or `File -> Export 3D plot` with shortcut `Ctrl + T` in the menu bar.

## Viewing chromatograms

When some model is loaded you can view the chromatogram in different ways

There are 4 tabs for viewing the data.

The tabs can be dragged around by dragging the tab header.
This way it is possible to change the layout of the program and to have some views side-by-side.

Double clicking a tab header will open that tab in a new window.
Closing that window will bring it back to the original window.

### 2d view

This is probably the most important view.

The 2d view has on the x axis the times from the first chromatography column, and on the y axis the times of the second chromatography column.

The 2d view is also used to define the integration areas.

The status bar will show the x, y and z location of the mouse position.
The x and y are the location of the mouse, measured in number of values from the origin.
The z is the value on that mouse position.

#### controls

The graph can be moved by dragging it with the mouse.
Scrolling will zoom in and out.

To scroll each axis independently, scroll with the mouse over the axis that you want to scoll.
Alternatively it is possible to do this by dragging while the right mouse button is pressed.

### 1d view

The 1d view shows the graph that you get when summing all the datas from the columns of the 2d view (column refers here to table column, not the chromatograpy column).

The status bar will show the x location of the mouse on the graph, and as y value the value of the graph at that x location (so not the y location of the mouse!).

The controls are the same as for the 2d view.

### 3d view

The 2d view will allow looking at the graph in 3d.

Only the selected integration areas will be shown.

#### Controls

Drag the mouse to rotate the viewpoint around.
Scroll to zoom in or out further.
Drag with the mouse wheel to move the viewpoint left/right/up/down.

### Integration list

This is not a view of the chromatogram but a list of all integration areas.

The integration areas can be selected by clicking on them.

The label for inegration areas can be changed by double-clicking the current label and entering a new one.


## Integration areas

A new integration area can be created using `Edit -> Draw selection` in the menu bar, clicking `Draw selection` in the toolbar or with the Ctrl-d keyboard shortcut.

It will create a default location for an integration area defined by 3 control points.

In the 2d view selected integration areas have a solid read line, while not selected areas have a broken red line.


### Defining integration areas

The control points can be moved around by clicking on them and dragging (in the 2d view).
The whole integration area can be moved around by clicking within the area and dragging.
More control points can be added by clicking on one of the lines that defines the area.
A control point can be removed by right-clicking it and clicking `Remove handle`.
Removing control points is not possible if there are only 3 control points.

### Integration area information

In the Integration list tab there is information on the integration area.
It has the label (can be changed), the mean of the values in that area.

If the `Show transformed data` option is on, and there is a transformation, the values of the sum and the mean are about the graph after the transformation.


## Transformations

Several transformations over the data can be chosen.

These will affect the data in the 1d, 2d, and 3d view, and the values in the integration list.

`Show transformed data` can be toggled to quickly switch between the transformed view and the raw data view.

The transformation can be chosen with the `Set transformation` option in the toolbar or in the menu bar (under `Tools`).
This dialog allows choosing the transformation and its parameters.
Pressing 'Confirm' or 'Apply' will actually apply the transformation.

If a transformation is chosen when another transformation already exists, the new transformation will replace the old transformation.
It is not possible to combine multiple transformations.

### Static cut-off

Substract the given value from all points in the graph.

### Dynamic cut-off

This has 2 modes.

A percentage can be chosen which will be called `n` here.

With 'column' a column of the graph is meant, not the physical columns for the chromatography.

A percentage of `0` with either mode would subtract just the minimum value from a column from that entire column.

#### Mean

Take the mean of the lowest `n` percent of the values in a column, and subtract that value from all values in the column.

#### Max

Take the mean of the lowest `n` percent of the values in a column, and subtract that value from all values in the column.

### Gaussian convolution

Performs a simple gaussian filter on the data.
See [https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.ndimage.filters.gaussian_filter.html](https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.ndimage.filters.gaussian_filter.html).

The mode is 'constant' and cval is the default of 0.0

### Min1d convolution

This mode will take the sums of all values in a column.

This 1d list of sums is then passed through a min filter, which compares the sum to the sums nearby columns, and takes the min of that.

This resulting value is then divided by the length of the column (the height of the graph), and subtracted from each value in that column.

### Custom convolution

It is possible to load in a custom convolution from a csv file.

This file should have a grid of numbers that represent the convolution matrix.
In `exampledata/convolutions/` are some example convolution csv files.

The convolution is done by [https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.convolve.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.convolve.html).
The mode is 'constant' again.

## Palettes

It is possible to choose color palettes in the `Choose palette` dialog.
Apart from the default palettes, this list is taken from the `.2D-GC/palettes/` directory in the user home directory.

When saving a project, the current palette of the project is also saved in the `.gcgc` file.


### Custom Color Palettes
User defined color palettes can be imported from the `choose palette` dialog.
Imported palettes are saved into `~/.2D-GC/palettes/` (where `~` stands for the user home directory).
Custom Palettes can be defined in a plain text file ending with `.palette`, with each line containing the comma separated rgb values defining a color, each component can have a value from 0-255. 
The first line is the color for the lowest value, the last line is the color for the highest value.

For example, the common color palette jet can be defined like so:

#### jet.palette:
```
  0,   0, 127
  0,   0, 255
  0, 127, 255
  0, 255, 255
127, 255, 127
255, 255,   0
255, 127,   0
255,   0,   0
127,   0,   0
```
**NOTE:** Spaces and leading zeros are ignored. `0 ,   001,000 == 0,1,0`

Some more examples can be found in the `exampledata/palettes/` directory.
