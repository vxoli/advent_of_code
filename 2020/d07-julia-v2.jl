#!/usr/bin/env julia
# copied from fgcv
# https://github.com/rgcv/aoc2020/blob/main/07/run.jl

parsebags(filename) =
    let bagmap = Dict{String,Array{Pair{String,Int}}}()
        for line ∈ eachline(filename)
            root = match(r"(.*?) bags contain", line).captures[1]
            start = SubString(line, last(findlast("contain ", line)))
            children = match.(r"(\d+) (.*?) bags?[,.]?$", split(start, ","))
            foreach(children) do child
                get!(bagmap, root, [])
                if !isnothing(child)
                    count, name = child.captures
                    push!(bagmap[root], string(name) => parse(Int, count)) 
                end
            end
        end
        bagmap
    end

dfs(graph, root, visited = []) =
    let total = 0
        root ∈ visited || push!(visited, root)
        foreach(graph[root]) do (child, count)
            _, nc = dfs(graph, child, visited)
            total += count * (nc + 1)
        end
        visited, total
    end
dfs(graph) = root -> dfs(graph, root)

alldfs(graph) = map(dfs(graph), [keys(graph)...])

if abspath(PROGRAM_FILE) == @__FILE__
    filename = joinpath(@__DIR__, "d07-input.txt")
    # part 1
    println("Part 1: How many bag colors can eventually contain at least one shiny gold bag? Answer: ", count(path -> "shiny gold" ∈ path[2:end],
                first.(alldfs(parsebags(filename)))))
    # part 2
    println("Part 2: How many individual bags are required inside your single shiny gold bag? Answer: ", last(dfs(parsebags(filename), "shiny gold")))
end
