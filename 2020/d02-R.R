# read input data
data <- readLines('d02-input.txt')
passwords <- do.call(rbind, strsplit(data, '[- ]|\\: '))
passwords <- setNames(as.data.frame(passwords), c('min','max','letter','password'))
passwords <- transform(passwords, min = as.integer(min), max = as.integer(max))

with(passwords, {
    n <- stringr::str_count(password,letter)
    sum(n >= min & n <= max)
})