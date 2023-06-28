def main():
    val_shapes = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    score = 0
    with open("input.txt") as file:
        for line in file:
            p_1, p_2 = line.split()

            score += val_shapes[p_2]

            # Draw
            if val_shapes[p_1] == val_shapes[p_2]:
                score += 3
            # Win (shape to beat p_1 is next in sequence)
            elif (val_shapes[p_1]+1)%3 == val_shapes[p_2]%3:
                score += 6

    print(score)
            

if __name__ == "__main__":
    main()