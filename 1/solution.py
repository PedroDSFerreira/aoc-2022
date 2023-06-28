def main():
    elves = [0]
    with open("input.txt") as file:
        for line in file:
            if line.strip():
                elves[-1] += int(line.strip())
            else:
                elves.append(0)
    
    print(max(elves))
            

if __name__ == "__main__":
    main()