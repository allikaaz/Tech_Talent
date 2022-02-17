a <- c(2,4,6,8,10)
b <- c(1,3,5,7,9)
c <- c(12,14,15,17,18)
d <- cbind(a,b,c)
# first method
e <- matrix((d),nrow = 3, ncol = 5)
print(e)
# Second method
f <- rbind(a,b,c)
g <- matrix((f),nrow = 3, ncol = 5)
print(g)

# plotting the graph

install.packages("ggplot2")
library(ggplot2)
matplot(g, type ="o", pch=15, col=1:5)

# Q2. Creating dataframe for 5 employees
employees <- data.frame(
  Names = c("Andy", "Georgina","Miranda","Sarah", "Kazeem"),
  Ages = c(40,25,30,32,35),
  Roles = c("Recruiter","Trainer", "Director","Manager","Trainee"),
  Service_year = c(5,2,4,6,1)
)
print(employees)

# Q3 Plotting using qplot function
x <- seq(1:20)
y <- x^2
qplot(x,y)

# Q4, creating simple bar chart for five subjects

x <- c("Maths", "English","Chemistry","physics","science")
y <- c(75,54,43,62,70)
barplot(y, names.arg=x, col="green")

# Q5, user input

name <- readline("Enter your name pls: ")
paste("Welcome", name)
age <- readline("Enter your age number: ")
paste("Your age is", age)


# Q6, creating sequence of numbers
Numb <- seq(20:50)
Nmen <- mean(Numb)
Nsum <- sum(Numb)
print(Nsum)
print(Nmen)

# Q7, Generating 10 random integer between -50 & 50
# method 1
A <- runif(10, min = -50, max = 50)
print(A)

#method 2
set.seed(456)
B <- sample(-50:50, 10, replace = FALSE)
print(B)
