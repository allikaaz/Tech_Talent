diamonds
mpg

#boxplot  with qplot

ggplot2::mpg

qplot(data = mpg, x = cty, y = hwy, geom = "boxplot", color = class)

#boxplot  with qplot
qplot(data = mpg, x = cty, y = hwy, geom = "line", color = class)

#Point plot  with qplot
qplot(data = mpg, x = cty, y = hwy, geom = "point", color = class)

# bar plot and stacked bar plot

ggplot2::diamonds

?diamonds
diamonds

qplot(data = diamonds, y = clarity, geom = "bar", fill = cut)

# boxplot
qplot(data = diamonds, y = clarity, geom = "boxplot", fill = cut)