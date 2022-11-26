def election(*args:bool) -> bool:
    return max(args,key=args.count)
print(election(0,0,1))