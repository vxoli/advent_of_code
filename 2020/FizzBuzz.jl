#FizzBuzz
start = 0
finish = 100

for count = start:finish
    FizzBuzzString = ""
    if (count % 3 == 0) & (count % 5 == 0)
        FizzBuzzString = "FizzBuzz"
    elseif (count % 3 == 0) & (count % 5 != 0)
            FizzBuzzString = "Fizz"
    elseif (count % 3 != 0) & (count % 5 == 0)
            FizzBuzzString = "Buzz"
    else
        FizzBuzzString = string(count)
    end
    println(FizzBuzzString)
end

# Rockstar version
# z(i)=(f=i .%[3,5] .==0;sum(f)>0 ? foldl(*,["Fizz","Buzz"][f]) : i)
# println.(z.(1:100))

    
