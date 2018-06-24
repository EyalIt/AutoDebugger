import trace
import func_utils
import sys

def run(func):
    amountOfRuns = 10
    tracer = trace.Trace(count=1, trace=0)
    argsGen = func_utils.getArgsGenerator(func)

    for i in range(amountOfRuns):
        # execute the function with a tracer
        func_utils.execute(func, argsGen, tracer)

        # get the code coverage results and find what is there to improve
        coverage = beautify_coverage(func, tracer.results())
        index = get_row_with_min_coverage(coverage)

        # find out how to improve the coverage (if possible)
        iterateCode(coverage, index, argsGen)

def iterateCode(coverage, index, argsGen):
    print index, coverage
    for i in range(index - 1, 0, -1):
        code = coverage[i]["code"]
        if ("if" in code):
            condition = parseCondition(code)
            updateLimitation(condition, argsGen)

def parseCondition(code):
    # print scopeLevel(code)
    index = code.index("if", 0)
    return splitToTokens(code[index + len("if "):])

def splitToTokens(code):
    # remove the parenthesis
    start = code.index("(", 0) + 1
    end = code.index(")", 1)
    cond = code[start:end]

    tokens = cond.split(" ")
    return tokens

def scopeLevel(code):
    tab = 4
    count = 0

    while (code[count] == ' '):
        count += 1

    return count / tab

def updateLimitation(condition, argsGen):
    symbol = condition[0]
    cond = condition[1]
    value = int(condition[2])

    for gen in argsGen:
        if (gen.getSymbol() == symbol):
            if (cond == '>'):
                gen.setMinValue(value + 1)

            if (cond == '<'):
                gen.setMaxValue(value - 1)

def test(func):
    number_of_executes = 100

    tracer = trace.Trace(count=1, trace=1)
    for i in range(number_of_executes):
        func_utils.execute(func, tracer)

    results = tracer.results()

    # beautify coverage results
    b_coverage = beautify_coverage(func, results)
    index = get_row_with_min_coverage(b_coverage)
    print b_coverage[index]["code"]

def print_coverage(coverage):
    for k, v in coverage.counter.iteritems():
        print k
        print v

def beautify_coverage(func, coverage):
    lines, first_line = func_utils.get_source_lines(func)
    length = len(lines)
    count = [0] * length

    for k, v in coverage.counter.iteritems():
        _, number = k
        count[number - first_line] += v

    res = []
    for i in range(length):
        if (lines[i] != '\n'):
            res.append({"line": first_line + i, "code": lines[i], "count" : count[i]})

    return res

def get_row_with_min_coverage(coverage):
    min = sys.maxint
    index = 0

    # iterate all lines of code, skip the function's signature
    for i in range(1, len(coverage)):
        if (coverage[i]["count"] < min):
            min = coverage[i]["count"]
            index = i

    return index
