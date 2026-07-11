"""
Code sample demonstrating generators
- generators return an iterator
- instead of computing all values up front and returning a list
- generators product one value at a time, pausing computation between
- utilizes yeild rather than return
- function is frozen until next() invoked

## why use them?
    1. memory effecient
    2. can handle incredibly large sequences
    3. can be used for dynamic data pipelines
 """

## regular function
## builds the entire array in memory before returning
def squares(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

squares(10)

# generator function
# lazy -- builds next value based on next() 
def squares_gen(n):
    for i in range(n):
        yield i * i

generate_object = squares_gen(5)

# let's check type
type(generate_object)

# let's call next() a few times!
print(f'{next(generate_object)=}')
print(f'{next(generate_object)=}')
print(f'{next(generate_object)=}')
print(f'{next(generate_object)=}')
print(f'{next(generate_object)=}')
print(f'{next(generate_object)=}')

# check what happens when we run out of values
try: 
    print(f'{next(generate_object)=}')
except StopIteration:
    print("generator is exhausted")


